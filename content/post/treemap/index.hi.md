---
title: अभिलेखागार का एक दृश्य ब्राउज़र
subtitle: डिजिटल रूप में ढले अभिलेखीय दस्तावेज़ों तक पहुँचने का सहज तरीक़ा

# Summary for listings and search engines
summary: इंटरैक्टिव विज़ुअलाइज़ेशन पाठकों को जटिल अभिलेखीय दस्तावेज़ों में घूमने-फिरने के लिए एक वैकल्पिक इंद्रिय-सहारा देते हैं।

# Link this post with a project
projects: [Making & Knowing Project]

# Date published
date: "2021-06-20T16:00:00Z"

# Date updated
lastmod: "2021-06-20T17:00:00Z"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false
machine_translated: true

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: ''
  focal_point: ""
  placement: 1
  preview_only: true

authors:
- clement

tags:
- डिजिटल मानविकी
- डेटा विज़ुअलाइज़ेशन
- अभिलेखागार अनुसंधान

categories:
- टिप्पणियाँ
---
# समस्या
डिजिटल संस्करण एक विरोधाभास से ग्रस्त हैं: एक ओर वे दुरूह दस्तावेज़ों को व्यापक जनता तक पहुँचाते हैं, दूसरी ओर उनके अभौतिक हो जाने से जो इंद्रिय-अनुभव खो जाता है, वह पाठकों को भटका देता है, यहाँ तक कि उन्हें सामग्री से जुड़ने से हतोत्साहित भी कर देता है। दस्तावेज़ों के विशाल भंडारों में रास्ता ढूँढ़ना बोझिल और डराने वाला काम बन जाता है। यह सिर्फ़ उन पाठकों की बात नहीं है जिन्हें अभिलेखागार अनुसंधान का अनुभव नहीं; संज्ञानात्मक अक्षमताओं से प्रभावित पाठकों के लिए भी यह उतना ही सच है।

# समाधान
यहीं अभिलेखीय मेटाडेटा हमारे काम आ सकता है। दरअसल ऐसे डेटा से हम इंटरैक्टिव दृश्य-अमूर्तन रच सकते हैं, जो पाठकों को एक वैकल्पिक इंद्रिय-सहारा देते हैं और इस तरह सुविधा और सुगमता दोनों बढ़ाते हैं। अभिलेखागार को आँखों से घूमने लायक़ बनाने के लिए एक ट्रीमैप – या कोई भी आरेख जो श्रेणीबद्ध डेटा को कुशलता से खोलकर दिखाए – काम कर जाता है। 

# प्रयोग
मेरा पहला प्रयोग `D3.js` के लिए बने [Zoomable Treemap कोड](https://observablehq.com/@d3/zoomable-treemap) को अपनाता है और उसमें हाइपरलिंक जोड़ता है। यह पांडुलिपि BnF Ms Fr 640, उसके फ़ोलियो, और हर फ़ोलियो के भीतर की प्रविष्टियों को दर्शाता है। रंग प्रमुख श्रेणी दिखाते हैं। हर प्रविष्टि पर कर्सर ले जाने से और जानकारी मिलती है, पांडुलिपि का हाइपरलिंक भी।   
इस तरह ट्रीमैप एक इंटरैक्टिव दृश्य अनुक्रमणिका बन जाता है, जो पाठकों को बहुत तेज़ और सजीव झलक देता है – न सिर्फ़ पांडुलिपि की विषय-वस्तु की, बल्कि हर फ़ोलियो और हर प्रविष्टि के आकार की भी।  
~~आने वाले महीनों में मैं इस विचार पर प्रयोग जारी रखूँगा, दूसरे आरेख और दूसरी श्रेणी-व्यवस्थाएँ आज़माते हुए… इंतज़ार कीजिए!~~ ट्रीमैप के नए संस्करण के लिए [यहाँ]({{< relref "/post/treemap2" >}}) क्लिक करें।  
> [!NOTE]
> बेहतर अनुभव के लिए वेबपेज की सेटिंग Light मोड में रखें (ऊपर दाईं ओर चंद्रमा के आइकन पर क्लिक करें)।

  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title></title>
    <link rel="preconnect" href="https://fonts.gstatic.com" />
    <link
      href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap"
      rel="stylesheet" />
    <link rel="stylesheet" href="css/index.css" />
    <link rel="stylesheet" href="css/vis-treemap.css" />
    <link rel="stylesheet" href="css/vis-tooltip.css" />
  </head>
  <body>
    <p>Click any cell to zoom in, or the top to zoom out.</p>
    <div id="treemap"></div>
    <script src="https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js" integrity="sha384-CjloA8y00+1SDAUkjs099PVfnY2KmDC2BZnws9kh8D/lX1s46w6EPhpXdqMfjK6i" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="js/vis-treemap.js"></script>
    <script src="js/vis-tooltip.js"></script>
    <script src="js/index.js"></script>
  </body>