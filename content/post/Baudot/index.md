---
title: "Teaching Binary with the ITA2 Telegraph Emulator"
subtitle: "A hands-on approach to understanding early digital communication"
summary: An interactive demonstration of the ITA2 (Baudot-Murray) telegraph code that helps students grasp fundamental concepts of binary encoding and state machines
projects: [""]
date: "2025-02-13T00:00:00Z"
lastmod: "2025-02-13T00:00:00Z"
draft: false
featured: false
image:
  caption: 'ITA2 Telegraph tape showing encoded message'
  focal_point: ""
  placement: 2
  preview_only: false
authors:
- admin
tags:
- Digital History
- Programming
- Teaching
- Historical Computing
categories:
- Digital Humanities
- Teaching Tools
---

## Making Abstract Concepts Tangible

This ITA2 emulator is a practical teaching aid. By making abstract encoding concepts visible and interactive, it intorduces students to several key concepts in computing and telecommunications, such as binary representation - how text becomes patterns of 1s and 0s.

While we often teach this abstractly, seeing the actual holes appear helps students grasp how physical systems can represent digital information.

{{< Baudot >}}

## Historical Context: From Telegraph to Computing

The ITA2 (International Telegraph Alphabet No. 2) code, also known as the Baudot-Murray code, was developed in the 1920s as a refinement of Émile Baudot's original telegraph code from the 1870s. These early telecommunication systems had a direct influence on later computing developments:

- The 5-bit encoding scheme was an early example of character encoding
- The character set limitations (only 32 possible combinations with 5 bits) led to the ingenious LETTERS/FIGURES shift mechanism
- This system was used well into the 20th century for teletype machines

## Learning State Machines Through Play

The LETTERS/FIGURES shift mechanism introduces state machines naturally. Students discover through experimentation that the same pattern can represent different characters depending on the current mode. This hands-on experience with state-based encoding prepares them for more complex computing concepts.

For example, the bit pattern `00011` represents:
- The letter 'A' when in LETTERS mode
- The number '1' when in FIGURES mode

This dual interpretation based on state is fundamental to how computers work with data.

## Classroom Activities

Here are some ways to incorporate the ITA2 emulator into teaching:

1. **Code Breaking Challenge**: Have students decode messages encoded as ITA2 patterns
2. **Efficient Encoding**: Discuss why the shift mechanism was important for saving bandwidth
3. **Evolution of Encoding**: Compare ITA2's 5-bit code to ASCII (7-bit) and Unicode
4. **Physical Computing**: Connect this historical system to modern microcontrollers like Arduino

## Accessibility Benefits

Beyond its historical interest, this approach helps students with different learning styles:
- Visual learners see the patterns
- Kinesthetic learners interact directly with the encoding process
- Conceptual thinkers can explore the mathematical aspects of information theory

## Implementation Details

The emulator is implemented in JavaScript and can be easily integrated into any web-based learning platform. The code is modular and customizable for different teaching contexts.

You can find the source code and try the emulator yourself at: [GitHub Repository](https://github.com/Pantagrueliste/BaudotMurray_Emulator)