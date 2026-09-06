---
title: "tei-mcp v0.3: Encoding TEI Without Rewriting the Source"
subtitle: Span-locked composition makes body-text hallucinations impossible by construction

summary: >
  The new release of tei-mcp introduces span-locked composition, a system
  designed to prevent the most damaging class of hallucination in
  AI-assisted TEI encoding: silent rewrites of the source text. The model
  never types body text; it registers tags as offsets over the source,
  and the composer refuses to return any TEI whose flat text content
  differs from the original by a single byte.

date: "2026-05-05T00:00:00Z"
lastmod: "2026-05-05T00:00:00Z"

draft: false
featured: true

authors:
- clement

tags:
- Digital Humanities
- TEI
- MCP
- AI

categories:
- Digital Humanities
---

When I [first wrote about tei-mcp](/post/tei-mcp/), the goal was to stop
AI assistants from hallucinating TEI markup. Schema grounding solved part
of the problem: with direct, tool-based access to the P5 specification,
the model no longer has to guess what an element means or which attributes
it accepts. The output validates.

But hallucination has two faces in TEI encoding, and the schema only
catches one of them. Validating against the spec tells you the *markup*
is well-formed. It says nothing about the *text* that markup wraps. And
that — the text itself — is where the more damaging hallucinations live.
Span-locked composition, the headline feature in v0.3, is designed
specifically to prevent them.

{{< toc >}}

## The hallucination the schema cannot catch

Ask a model to encode a sixteenth-century French letter and you will often
get back a TEI document that looks impeccable. The header is filled in, the
`<persName>` tags are placed correctly, the `<dateline>` is well-formed. Run
it through `validate_document` and it passes.

Then diff the body against the source.

`mesme` has become `même`. A comma has migrated. `luy` has been silently
modernised to `lui`. A clause that was hard to read in the manuscript has
been "corrected" into something cleaner. None of these changes were
requested. None of them are flagged. The document is schema-valid and
quietly wrong.

For an archival workflow — where the encoded text becomes the permanent
record that downstream readers, search indexes, and citations rely on —
this is the failure mode that matters most. A malformed tag is annoying.
A modernised spelling that nobody notices for five years is a corruption.

## Span-locked composition

The new release (v0.3) ships a hallucination-prevention mechanism aimed
squarely at this failure mode. The design goal is to make body-text
hallucinations impossible by construction, not merely unlikely.

The idea is simple: **the model never types body text**.

Instead, the workflow goes like this:

1. The model calls `get_source("letter_001")` and receives the source
   plaintext as an immutable string.
2. For each tag it wants to apply, it calls
   `tag_span("letter_001", start, end, element_path, attrs)` — registering
   a TEI element at a character range over the source.
3. When it is done, it calls `compose("letter_001")`. The server interleaves
   the recorded tags with the original plaintext, renders the final TEI,
   and then verifies *byte-by-byte* that the flat text content of the
   rendered document equals the source.

If the bytes match, the document comes back. If they don't — if the model's
tags somehow imply a body that differs from the source by even a single
character — `compose()` raises rather than returning a corrupted document.

There is no path through this workflow in which the model produces a
TEI document whose body text differs from the source. The invariant is
mechanical, not behavioural. You don't have to trust the model not to
hallucinate; you have to trust a `==` check between two byte strings.

## What this is, and what it isn't

Span-locked composition is **complementary** to schema grounding, not a
replacement. The schema-grounding tools (`validate_document`,
`lookup_element`, `valid_children`, and the rest of the original sixteen)
help the model produce *valid* TEI. Span-locked composition guarantees
that the body text inside that TEI is *faithful* to the source. A
deployable encoding workflow has to satisfy both axes, and now both are
covered by a single server.

It is also not a magic fix for everything. `compose()` does not yet check
that the registered tags are admissible per a loaded ODD customisation —
that is a follow-up. Recorded tags live in process memory and don't
survive a restart. And the source files have to be readable from wherever
the server runs. These are all addressable; none of them undermine the
core invariant.

## Why this matters beyond TEI

The pattern generalises. Any time a model is asked to annotate, transform,
or wrap a piece of text — and any time the integrity of the underlying
text matters more than the model's ability to "improve" it — the same
shape of solution applies. Don't ask the model to retype the text. Ask
it to produce instructions over the text, and let a deterministic
composer apply them under an equality invariant.

For digital editions specifically, this changes what you can responsibly
ask a model to do. Encoding suddenly becomes a task you can delegate
without having to manually diff every output against the source. The
machine takes the boring path; the editor reviews the markup, not the
spelling.

## Getting the update

If you already have tei-mcp installed:

```bash
uvx tei-mcp@latest
```

Or fresh:

```bash
pip install tei-mcp
```

To use span-locked composition, point the server at a directory of source
plaintext files:

```bash
export TEI_MCP_SPAN_SOURCE_ROOT=/path/to/sources
uvx tei-mcp
```

Each file's stem becomes its document ID (`letter_001.txt` →
`letter_001`).

Source code, full documentation, and the design notes for the invariant:
[github.com/Pantagrueliste/tei-mcp](https://github.com/Pantagrueliste/tei-mcp)
