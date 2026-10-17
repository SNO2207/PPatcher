# Parallels Licensing Evidence

Static IDA and Hex Rays excerpts from prl_disp_service, SHA256 d9f2fff825b4e97400bfffb110b96b242d246d93aa3f4da05308f3e4319d6c26. Addresses are IDA virtual addresses at image base 0x100000000. Excerpts are selected lines, not complete functions. Decompiled types and argument labels can be inaccurate, especially for ARM64 return objects passed through X8. Analysis is read only.

## S1 Account request builder

`0x1003fef54`

```cpp
     // ... excerpt omitted ...
 119   {
 120     case 0:
 121       if ( off_10071DB80[0] != nullptr )
 122         v13 = strlen(__s: off_10071DB80[0]);
     // ... excerpt omitted ...
 125       v79 = (QArrayData *)QString::fromAscii_helper(this: (QString *)off_10071DB80[0], a2: (const char *)v13, a3: v7);
 126       v86.var0 = (void *)QString::fromAscii_helper(this: (QString *)"auth", a2: (const char *)4, a3: v23);
 127       QVariant::QVariant(this: (QVariant *)__p, a2: &v86);
 128       sub_10014D6A8(a1: (int)&v87, a2: (QString *)&v79);
     // ... excerpt omitted ...
 153 LABEL_54:
 154       if ( off_10071DB98[0] != nullptr )
 155         v28 = strlen(__s: off_10071DB98[0]);
 156       else
 157         v28 = 0xFFFFFFFFLL;
 158       v79 = (QArrayData *)QString::fromAscii_helper(this: (QString *)off_10071DB98[0], a2: (const char *)v28, a3: v24);
 159       QVariant::QVariant(this: (QVariant *)__p, a2: (const QString *)this + 6);
 160       sub_10014D6A8(a1: (int)&v87, a2: (QString *)&v79);
     // ... excerpt omitted ...
 173 LABEL_96:
 174       if ( off_10071DBA0[0] != nullptr )
 175         v47 = strlen(__s: off_10071DBA0[0]);
 176       else
 177         v47 = 0xFFFFFFFFLL;
 178       v79 = (QArrayData *)QString::fromAscii_helper(this: (QString *)off_10071DBA0[0], a2: (const char *)v47, a3: v44);
 179       QString::toUtf8_helper(this: (QString *)this + 8, a2: v51);
 180       QCryptographicHash::hash(a1: &v84, a2: &v83, a3: 1);
 181       QByteArray::toHex(this: (QByteArray *)&v84);
 182       v53 = nullptr;
 183       v54 = (QString *)((char *)v85 + *((_QWORD *)v85 + 2));
     // ... excerpt omitted ...
 295       goto LABEL_188;
 296     case 1:
 297       if ( off_10071DC30[0] != nullptr )
 298         v11 = strlen(__s: off_10071DC30[0]);
 299       else
 300         v11 = 0xFFFFFFFFLL;
 301       v79 = (QArrayData *)QString::fromAscii_helper(this: (QString *)off_10071DC30[0], a2: (const char *)v11, a3: v7);
 302       QVariant::QVariant(this: (QVariant *)__p, a2: off_10071DC38[0]);
 303       sub_10014D6A8(a1: (int)&v87, a2: (QString *)&v79);
 304       QVariant::~QVariant(this: (QVariant *)__p);
     // ... excerpt omitted ...
 316 LABEL_33:
 317       if ( off_10071DC48[0] != nullptr )
 318         v18 = strlen(__s: off_10071DC48[0]);
 319       else
 320         v18 = 0xFFFFFFFFLL;
 321       v79 = (QArrayData *)QString::fromAscii_helper(this: (QString *)off_10071DC48[0], a2: (const char *)v18, a3: v15);
 322       QVariant::QVariant(this: (QVariant *)__p, a2: (const QString *)this + 12);
 323       sub_10014D6A8(a1: (int)&v87, a2: (QString *)&v79);
     // ... excerpt omitted ...
 365       goto LABEL_179;
 366     case 2:
 367       if ( off_10071DC30[0] != nullptr )
 368         v14 = strlen(__s: off_10071DC30[0]);
 369       else
 370         v14 = 0xFFFFFFFFLL;
 371       v79 = (QArrayData *)QString::fromAscii_helper(this: (QString *)off_10071DC30[0], a2: (const char *)v14, a3: v7);
 372       QVariant::QVariant(this: (QVariant *)__p, a2: off_10071DC40[0]);
 373       sub_10014D6A8(a1: (int)&v87, a2: (QString *)&v79);
 374       QVariant::~QVariant(this: (QVariant *)__p);
     // ... excerpt omitted ...
 386 LABEL_62:
 387       if ( off_10071DC48[0] != nullptr )
 388         v32 = strlen(__s: off_10071DC48[0]);
 389       else
 390         v32 = 0xFFFFFFFFLL;
 391       v79 = (QArrayData *)QString::fromAscii_helper(this: (QString *)off_10071DC48[0], a2: (const char *)v32, a3: v29);
 392       QVariant::QVariant(this: (QVariant *)__p, a2: (const QString *)this + 12);
 393       sub_10014D6A8(a1: (int)&v87, a2: (QString *)&v79);
     // ... excerpt omitted ...
 428       goto LABEL_178;
 429     case 3:
 430       if ( off_10071DC50[0] != nullptr )
 431         v12 = strlen(__s: off_10071DC50[0]);
 432       else
 433         v12 = 0xFFFFFFFFLL;
 434       v79 = (QArrayData *)QString::fromAscii_helper(this: (QString *)off_10071DC50[0], a2: (const char *)v12, a3: v7);
 435       QVariant::QVariant(this: (QVariant *)__p, a2: (const QString *)this + 13);
 436       sub_10014D6A8(a1: (int)&v87, a2: (QString *)&v79);
     // ... excerpt omitted ...
 449 LABEL_41:
 450       if ( off_10071DC58[0] != nullptr )
 451         v22 = strlen(__s: off_10071DC58[0]);
 452       else
 453         v22 = 0xFFFFFFFFLL;
 454       v79 = (QArrayData *)QString::fromAscii_helper(this: (QString *)off_10071DC58[0], a2: (const char *)v22, a3: v19);
 455       QVariant::QVariant(this: (QVariant *)__p, a2: (const QString *)this + 14);
 456       sub_10014D6A8(a1: (int)&v87, a2: (QString *)&v79);
     // ... excerpt omitted ...
 469 LABEL_79:
 470       if ( off_10071DC60[0] != nullptr )
 471         v40 = strlen(__s: off_10071DC60[0]);
 472       else
 473         v40 = 0xFFFFFFFFLL;
 474       v79 = (QArrayData *)QString::fromAscii_helper(this: (QString *)off_10071DC60[0], a2: (const char *)v40, a3: v37);
 475       QVariant::QVariant(this: (QVariant *)__p, a2: *((_BYTE *)this + 120));
 476       sub_10014D6A8(a1: (int)&v87, a2: (QString *)&v79);
     // ... excerpt omitted ...
 495       {
 496         v50 = (const char *)(off_10071DB98[0] != nullptr ? strlen(__s: off_10071DB98[0]) : 0xFFFFFFFFLL);
 497         v79 = (QArrayData *)QString::fromAscii_helper(this: (QString *)off_10071DB98[0], a2: v50, a3: v33);
 498         QVariant::QVariant(this: (QVariant *)__p, a2: (const QString *)this + 6);
 499         sub_10014D6A8(a1: (int)&v87, a2: (QString *)&v79);
     // ... excerpt omitted ...
 560     default:
 561       sub_1005756CC(a1: "", a2: "WebPortalCommunication", a3: 0, a4: "Unknown authorization type", v79);
 562       v4 = 0xFFFFFFFFLL;
 563 LABEL_189:
```

## S2 Successful sign in persists tokens

`0x10015cc20`

```cpp
     // ... excerpt omitted ...
  36
  37   if ( a2 < 0 )
  38   {
  39     LODWORD(v34) = 0x80000000;
     // ... excerpt omitted ...
  44   }
  45   sub_1001507D0();
  46   v3 = sub_1001506D0();
  47   v4 = (__int64)*(this + 6);
  48   if ( v4 != 0 && *(_DWORD *)(v4 + 4) != 0 )
     // ... excerpt omitted ...
  51     v5 = 0;
  52   sub_1003FEF04(a1: &v33, a2: v5);
  53   sub_1001500C8(a1: v3, a2: (void **)&v33);
  54   v7 = v33;
  55   if ( *(_DWORD *)v33 != -1 )
     // ... excerpt omitted ...
  69 LABEL_11:
  70   v8 = sub_1001506DC(a1: v7);
  71   v9 = (__int64)*(this + 6);
  72   if ( v9 != 0 && *(_DWORD *)(v9 + 4) != 0 )
     // ... excerpt omitted ...
  75     v10 = 0;
  76   sub_1003FEF28(a1: &v33, a2: v10);
  77   sub_1001500C8(a1: v8, a2: (void **)&v33);
  78   v12 = v33;
  79   if ( *(_DWORD *)v33 != -1 )
```

## S3 License command payloads

`0x100152ab8`

```cpp
     // ... excerpt omitted ...
 115     v13 = nullptr;
 116     v12 = (QString *)"";
 117   }
 118   else
     // ... excerpt omitted ...
 150 LABEL_25:
 151   if ( *a1 == 5 )
 152     goto LABEL_26;
 153   v29 = a1[1];
 154   if ( *a1 == 3 )
 155   {
 156     v30 = *((QArrayData **)a1 + 8);
     // ... excerpt omitted ...
 162   {
 163     v83[0] = (QArrayData *)QString::fromAscii_helper(this: (QString *)"", a2: nullptr, a3: v14);
 164   }
 165   sub_10014B870(a1: &v84, a2: v29 != 1, a3: v83);
     // ... excerpt omitted ...
 177 LABEL_55:
 178   v82.var0 = (void *)QString::fromAscii_helper(this: (QString *)"host", a2: (const char *)4, a3: v31);
 179   QVariant::QVariant(a1: v83, a2: &v84);
 180   sub_10014D6A8(a1: v4, a2: &v82);
     // ... excerpt omitted ...
 224             return result;
 225           v84.var0 = (void *)QString::fromAscii_helper(this: (QString *)"offline", a2: (const char *)7, a3: v71);
 226           QVariant::QVariant(this: (QVariant *)v83, a2: *((_BYTE *)a1 + 61));
 227           sub_10014D6A8(a1: v4, a2: &v84);
     // ... excerpt omitted ...
 238   }
 239   switch ( v38 )
 240   {
 241     case 5:
 242 LABEL_26:
 243       v18 = a1[14];
 244       v84.var0 = (void *)QString::fromAscii_helper(this: (QString *)"platform", a2: (const char *)8, a3: v14);
 245       QVariant::QVariant(this: (QVariant *)v83, a2: 3);
 246       sub_10014D6A8(a1: v4, a2: &v84);
     // ... excerpt omitted ...
 259 LABEL_31:
 260       v84.var0 = (void *)QString::fromAscii_helper(this: (QString *)"lic_edition", a2: (const char *)0xB, a3: v19);
 261       QVariant::QVariant(this: (QVariant *)v83, a2: v18);
 262       sub_10014D6A8(a1: v4, a2: &v84);
     // ... excerpt omitted ...
 281       {
 282         v84.var0 = (void *)QString::fromAscii_helper(this: (QString *)"dry_run", a2: (const char *)7, a3: v22);
 283         QVariant::QVariant(this: (QVariant *)v83, a2: 1);
 284         sub_10014D6A8(a1: v4, a2: &v84);
     // ... excerpt omitted ...
 299       v27 = *a1;
 300       if ( *a1 == 6 )
 301       {
 302 LABEL_45:
 303         v28 = (void *)QString::fromAscii_helper(this: (QString *)"token", a2: (const char *)5, a3: v22);
 304         goto LABEL_81;
 305       }
     // ... excerpt omitted ...
 344       sub_100154600(a1: &v84);
 345       v82.var0 = (void *)QString::fromAscii_helper(this: (QString *)"vendor_info", a2: (const char *)0xB, a3: v46);
 346       QVariant::QVariant(this: (QVariant *)v83, a2: &v84);
 347       sub_10014D6A8(a1: v4, a2: &v82);
     // ... excerpt omitted ...
 360 LABEL_91:
 361       v82.var0 = (void *)QString::fromAscii_helper(this: (QString *)"hw_id", a2: (const char *)5, a3: v47);
 362       sub_10014AA6C(a1: &v81);
 363       QVariant::QVariant(this: (QVariant *)v83, a2: &v81);
     // ... excerpt omitted ...
 393 LABEL_101:
 394       v82.var0 = (void *)QString::fromAscii_helper(this: (QString *)"build_number", a2: (const char *)0xC, a3: v50);
 395       sub_10014ADE4(a1: &v81);
 396       QVariant::QVariant(this: (QVariant *)v83, a2: &v81);
     // ... excerpt omitted ...
 431       return (QArrayData *)QArrayData::deallocate(this: result, a2: (QArrayData *)2, a3: 8u, a4: v54);
 432     case 6:
 433       v84.var0 = (void *)QString::fromAscii_helper(this: (QString *)"force", a2: (const char *)5, a3: v14);
 434       QVariant::QVariant(this: (QVariant *)v83, a2: 1);
 435       sub_10014D6A8(a1: v4, a2: &v84);
     // ... excerpt omitted ...
 448 LABEL_107:
 449       v84.var0 = (void *)QString::fromAscii_helper(this: (QString *)"lic_key", a2: (const char *)7, a3: v14);
 450       QVariant::QVariant(this: (QVariant *)v83, a2: (const QString *)a1 + 1);
 451       sub_10014D6A8(a1: v4, a2: &v84);
     // ... excerpt omitted ...
 470       {
 471         v84.var0 = (void *)QString::fromAscii_helper(this: (QString *)"prev_lic_key", a2: (const char *)0xC, a3: v56);
 472         QVariant::QVariant(this: (QVariant *)v83, a2: (const QString *)a1 + 2);
 473         sub_10014D6A8(a1: v4, a2: &v84);
     // ... excerpt omitted ...
 488       v61 = *a1;
 489       if ( *a1 == 6 )
 490       {
 491 LABEL_121:
 492         v62 = (void *)QString::fromAscii_helper(this: (QString *)"token", a2: (const char *)5, a3: v56);
 493         goto LABEL_153;
 494       }
     // ... excerpt omitted ...
 559 LABEL_167:
 560       v84.var0 = (void *)QString::fromAscii_helper(this: (QString *)"vendor_info", a2: (const char *)0xB, a3: v76);
 561       sub_100154600(a1: &v82);
 562       QVariant::QVariant(this: (QVariant *)v83, a2: &v82);
     // ... excerpt omitted ...
 565       goto LABEL_168;
 566     case 9:
 567       v84.var0 = (void *)QString::fromAscii_helper(this: (QString *)"session_id", a2: (const char *)0xA, a3: v14);
 568       QVariant::QVariant(this: (QVariant *)v83, a2: (const QString *)a1 + 9);
 569       sub_10014D6A8(a1: v4, a2: &v84);
     // ... excerpt omitted ...
 582 LABEL_127:
 583       v84.var0 = (void *)QString::fromAscii_helper(this: (QString *)"vendor_info", a2: (const char *)0xB, a3: v63);
 584       sub_100154600(a1: &v82);
 585       QVariant::QVariant(this: (QVariant *)v83, a2: &v82);
     // ... excerpt omitted ...
 618         return result;
 619       v84.var0 = (void *)QString::fromAscii_helper(this: (QString *)"deactivate_hw_id", a2: (const char *)0x10, a3: v66);
 620       QVariant::QVariant(this: (QVariant *)v83, a2: v69);
 621       sub_10014D6A8(a1: v4, a2: &v84);
```

## S4 License acceptance

`0x100279b54`

```cpp
     // ... excerpt omitted ...
  18
  19   if ( (sub_1004626AC(a1: a2, a2: a3) & 1) != 0 )
  20   {
  21     QJsonObject::QJsonObject(this: (QJsonObject *)v20);
     // ... excerpt omitted ...
  23     v22 = (QArrayData *)&QArrayData::shared_null;
  24     if ( (sub_1003190C8(a1: v20, a2, a3) & 1) == 0 )
  25     {
  26       sub_1005756CC(a1: "", a2: "disp", a3: 0, a4: "unable to parse license info");
     // ... excerpt omitted ...
  31       goto LABEL_10;
  32     v19[0] = (QArrayData *)QString::fromAscii_helper(this: (QString *)"offline", a2: (const char *)7, a3: v8);
  33     v23 = 0;
  34     v10 = sub_1000134AC(a1: v20, a2: v19, a3: &v23);
     // ... excerpt omitted ...
  58 LABEL_24:
  59         QJsonObject::operator=(this: (QJsonObject *)(a1 + 24), a2: (const QJsonObject *)v20);
  60         QString::operator=(this: (QString *)(a1 + 40), a2: (const QString *)&v21);
  61         QString::operator=(this: (QString *)(a1 + 48), a2: (const QString *)&v22);
     // ... excerpt omitted ...
  65       }
  66       sub_10027A494(a1: v19, a2: a1, a3: 3);
  67       sub_100279E74(a1: (int)v19, a2: (int)off_1006EF6D0[0], a3: a2);
  68       sub_100279E74(a1: (int)v19, a2: (int)off_1006EF6D8[0], a3);
  69       if ( (sub_10027A8B4(a1: v19) & 1) != 0 )
  70       {
  71         sub_10027A6F0(a1: v19);
  72         goto LABEL_24;
  73       }
  74       sub_1005756CC(a1: "", a2: "disp", a3: 0, a4: "unable to save license info");
  75       sub_10027A6F0(a1: v19);
  76       v15 = 4294910295LL;
  77 LABEL_27:
     // ... excerpt omitted ...
 106       QJsonObject::~QJsonObject(this: (QJsonObject *)v20);
 107       return v15;
 108     }
 109     v19[0] = (QArrayData *)QString::fromAscii_helper(this: (QString *)"is_trial", a2: (const char *)8, a3: v8);
 110     v23 = 0;
 111     v13 = sub_1000134AC(a1: v20, a2: v19, a3: &v23);
     // ... excerpt omitted ...
 134   }
 135   sub_1005756CC(a1: "", a2: "disp", a3: 0, a4: "Signature check failed for license info");
 136   return 4294910294LL;
 137 }
```

## S5 Stored license reload

`0x100279f58`

```cpp
     // ... excerpt omitted ...
  10
  11   sub_10027A494(a1: v9, a2: a1, a3: 1u);
  12   sub_10027A0B8(a1: (__int64 *)&v8, a2: (int)v9, __s: off_1006EF6D0[0]);
  13   sub_10027A0B8(a1: (__int64 *)&v7, a2: (int)v9, __s: off_1006EF6D8[0]);
  14   if ( *((_DWORD *)v8 + 1) != 0 && *((_DWORD *)v7 + 1) != 0 )
  15   {
  16     v3 = sub_100279B54((__int64)a1, a2: (QString *)&v8, a3: (QString *)&v7, a4: 0);
  17   }
  18   else
  19   {
  20     sub_1005756CC(a1: "", a2: "disp", a3: 0, a4: "Can't load license info.");
  21     v3 = 4294910296LL;
  22   }
  23   v4 = v7;
  24   if ( *(_DWORD *)v7 != -1 )
  25   {
  26     if ( *(_DWORD *)v7 != 0 )
  27     {
  28       if ( atomic_fetch_add((atomic_uint *volatile)v7, 0xFFFFFFFF) != 1 )
  29         goto LABEL_10;
  30       v4 = v7;
     // ... excerpt omitted ...
  35   v5 = v8;
  36   if ( *(_DWORD *)v8 != -1 )
  37   {
  38     if ( *(_DWORD *)v8 == 0 )
  39     {
  40 LABEL_14:
     // ... excerpt omitted ...
  43     }
  44     if ( atomic_fetch_add((atomic_uint *volatile)v8, 0xFFFFFFFF) == 1 )
  45     {
  46       v5 = v8;
     // ... excerpt omitted ...
  50 LABEL_15:
  51   sub_10027A6F0(a1: v9);
  52   return v3;
  53 }
```

## S6 Offline activation

`0x10020c760`

```cpp
     // ... excerpt omitted ...
  40   sub_10014F578(a1: &v37, a2: *(_QWORD *)(v39 + 8));
  41   if ( *(_DWORD *)(*(_QWORD *)v37 + 4LL) == 0 )
  42   {
  43     v20 = 4294956256LL;
     // ... excerpt omitted ...
  46   QString::toUtf8_helper(this: a3, a2: v6);
  47   QJsonDocument::fromJson(this: (QJsonDocument *)&v34, a2: nullptr, a3: v7);
  48   QJsonDocument::toVariant(this: (QJsonDocument *)&v35);
  49   QVariant::toMap(this: (QVariant *)v32);
  50   QVariant::~QVariant(this: (QVariant *)v32);
  51   QJsonDocument::~QJsonDocument(this: (QJsonDocument *)&v35);
  52   var0 = (QArrayData *)v34.var0;
  53   if ( *(_DWORD *)v34.var0 != -1 )
  54   {
  55     if ( *(_DWORD *)v34.var0 != 0 )
  56     {
  57       if ( atomic_fetch_add((atomic_uint *volatile)v34.var0, 0xFFFFFFFF) != 1 )
  58         goto LABEL_7;
  59       var0 = (QArrayData *)v34.var0;
     // ... excerpt omitted ...
  63 LABEL_7:
  64   v35.var0 = (void *)QString::fromAscii_helper(this: (QString *)"subscription", a2: (const char *)0xC, a3: v8);
  65   v11 = (QVariant *)sub_10015DBD4(a1: (int)&v36, a2: &v35);
  66   QVariant::toString(this: v11);
  67   v14 = (QArrayData *)v35.var0;
  68   if ( *(_DWORD *)v35.var0 != -1 )
  69   {
  70     if ( *(_DWORD *)v35.var0 != 0 )
  71     {
  72       if ( atomic_fetch_add((atomic_uint *volatile)v35.var0, 0xFFFFFFFF) != 1 )
  73         goto LABEL_12;
  74       v14 = (QArrayData *)v35.var0;
     // ... excerpt omitted ...
  78 LABEL_12:
  79   v34.var0 = (void *)QString::fromAscii_helper(this: (QString *)"signature", a2: (const char *)9, a3: v12);
  80   v15 = (QVariant *)sub_10015DBD4(a1: (int)&v36, a2: &v34);
  81   QVariant::toString(this: v15);
  82   v17 = (QArrayData *)v34.var0;
  83   if ( *(_DWORD *)v34.var0 != -1 )
  84   {
  85     if ( *(_DWORD *)v34.var0 == 0 )
  86     {
  87 LABEL_16:
     // ... excerpt omitted ...
  90     }
  91     if ( atomic_fetch_add((atomic_uint *volatile)v34.var0, 0xFFFFFFFF) == 1 )
  92     {
  93       v17 = (QArrayData *)v34.var0;
     // ... excerpt omitted ...
  97 LABEL_17:
  98   if ( *((_DWORD *)v32[0] + 1) != 0 && *((_DWORD *)v35.var0 + 1) != 0 )
  99   {
 100     v20 = sub_100279B54(a1: *(_QWORD *)(v39 + 8) + 48LL, a2: (QString *)v32, a3: &v35, a4: 3);
 101   }
 102   else
 103   {
 104     sub_1005756CC(a1: "", a2: "disp", a3: 0, a4: "Wrong format of data for offline activation");
 105     v20 = 4294967293LL;
 106   }
 107   v21 = (QArrayData *)v35.var0;
 108   if ( *(_DWORD *)v35.var0 != -1 )
 109   {
 110     if ( *(_DWORD *)v35.var0 != 0 )
 111     {
 112       if ( atomic_fetch_add((atomic_uint *volatile)v35.var0, 0xFFFFFFFF) != 1 )
 113         goto LABEL_26;
 114       v21 = (QArrayData *)v35.var0;
     // ... excerpt omitted ...
 119   v22 = v32[0];
 120   if ( *(_DWORD *)v32[0] != -1 )
 121   {
 122     if ( *(_DWORD *)v32[0] != 0 )
 123     {
 124       if ( atomic_fetch_add((atomic_uint *volatile)v32[0], 0xFFFFFFFF) != 1 )
 125         goto LABEL_31;
 126       v22 = v32[0];
     // ... excerpt omitted ...
 131   v23 = (QMapNodeBase **)v36;
 132   if ( *v36 != -1 )
 133   {
 134     if ( *v36 != 0 )
 135     {
 136       if ( atomic_fetch_add(v36, 0xFFFFFFFF) != 1 )
 137         goto LABEL_39;
 138       v23 = (QMapNodeBase **)v36;
 139     }
 140     if ( v23[2] != nullptr )
 141     {
 142       sub_100116438();
     // ... excerpt omitted ...
 150   v38 = nullptr;
 151   if ( v24 != nullptr && atomic_fetch_add(&v24->__shared_owners_, 0xFFFFFFFFFFFFFFFFLL) == 0 )
 152   {
 153     ((void (__fastcall *)(std::__shared_weak_count *))v24->__on_zero_shared)(a1: v24);
     // ... excerpt omitted ...
 160   sub_100209CDC(a1, this: (CVmEventBase *)v32);
 161   if ( (v20 & 0x80000000) == 0 )
 162   {
 163     v26 = (std::__shared_weak_count *)a2[1];
     // ... excerpt omitted ...
 165     v31 = v26;
 166     if ( v26 != nullptr )
 167       atomic_fetch_add_explicit(&v26->__shared_owners_, 1u, memory_order_relaxed);
 168     sub_1002098A4(a1: &v30, a2: 0);
 169     v27 = v31;
 170     if ( v31 != nullptr && atomic_fetch_add(&v31->__shared_owners_, 0xFFFFFFFFFFFFFFFFLL) == 0 )
 171     {
 172       ((void (__fastcall *)(std::__shared_weak_count *))v27->__on_zero_shared)(a1: v27);
     // ... excerpt omitted ...
 178   v28 = v38;
 179   if ( v38 != nullptr && atomic_fetch_add(&v38->__shared_owners_, 0xFFFFFFFFFFFFFFFFLL) == 0 )
 180   {
 181     ((void (__fastcall *)(std::__shared_weak_count *))v28->__on_zero_shared)(a1: v28);
     // ... excerpt omitted ...
 184   v29 = v40;
 185   if ( v40 != nullptr && atomic_fetch_add(&v40->__shared_owners_, 0xFFFFFFFFFFFFFFFFLL) == 0 )
 186   {
 187     ((void (__fastcall *)(std::__shared_weak_count *))v29->__on_zero_shared)(a1: v29);
```

## S7 License status

`0x10031a878`

```cpp
     // ... excerpt omitted ...
  37   if ( (QJsonObject::isEmpty(this: a1) & 1) != 0 )
  38     return 4294956296LL;
  39   __p = (void *)QString::fromAscii_helper(this: (QString *)"offline", a2: (const char *)7, a3: v2);
  40   LOBYTE(v34) = 0;
  41   v5 = sub_1000134AC(a1, a2: &__p, a3: &v34);
     // ... excerpt omitted ...
  66   QString::fromUtf8_helper(this: (QString *)p_p, a2: (const char *)v9, a3: v8);
  67   v11 = sub_100319F8C(a1, a2: &v34);
  68   v12 = v34;
  69   if ( *(_DWORD *)v34 != -1 )
     // ... excerpt omitted ...
  83       goto LABEL_24;
  84     return 4294910291LL;
  85   }
  86   operator delete(__p);
  87   if ( (v11 & 1) == 0 )
  88     return 4294910291LL;
  89 LABEL_24:
  90   v13 = sub_1003199DC(a1);
  91   if ( v13 == 0 )
  92     goto LABEL_36;
  93   v15 = v13;
  94   __p = (void *)QString::fromAscii_helper(this: (QString *)"is_trial", a2: (const char *)8, a3: v14);
  95   LOBYTE(v34) = 0;
  96   v17 = sub_1000134AC(a1, a2: &__p, a3: &v34);
     // ... excerpt omitted ...
 108 LABEL_30:
 109   if ( v15 < 28 )
 110     v19 = 1;
 111   else
 112     v19 = v17;
 113   if ( v15 != 27 && (v19 & 1) != 0 )
 114     return 4294956294LL;
 115 LABEL_36:
 116   __p = (void *)QString::fromAscii_helper(this: (QString *)"is_beta", a2: (const char *)7, a3: v14);
 117   LOBYTE(v34) = 0;
 118   v22 = sub_1000134AC(a1, a2: &__p, a3: &v34);
     // ... excerpt omitted ...
 131   if ( (v22 & 1) != 0 )
 132     return 4294956285LL;
 133   __p = (void *)QString::fromAscii_helper(this: (QString *)"platform", a2: (const char *)8, a3: v20);
 134   LODWORD(v34) = 5;
 135   v25 = sub_10001340C(a1, a2: &__p, a3: &v34);
     // ... excerpt omitted ...
 151 LABEL_48:
 152   if ( v25 != 3 && v25 != 0 )
 153     return 4294956292LL;
 154   result = sub_10002D8C8(a1);
 155   if ( (_DWORD)result == 0 )
 156     return result;
 157   __p = (void *)QString::fromAscii_helper(this: (QString *)"is_trial", a2: (const char *)8, a3: v27);
 158   LOBYTE(v34) = 0;
 159   v29 = sub_1000134AC(a1, a2: &__p, a3: &v34);
     // ... excerpt omitted ...
 172   if ( v29 != 0 )
 173     return 4294956295LL;
 174   else
 175     return 4294956222LL;
 176 }
```

## S8 Hardware binding

`0x100319f8c`

```cpp
     // ... excerpt omitted ...
  23
  24   v21.var0 = (void *)QString::fromAscii_helper(this: (QString *)"hosts", a2: (const char *)5, a3);
  25   QJsonObject::value(this: a1, a2: &v21);
  26   QJsonValue::toArray(this: (QJsonValue *)v24);
     // ... excerpt omitted ...
  53       QJsonValue::toObject(this: (QJsonValue *)v24);
  54       v19 = (QArrayData *)QString::fromAscii_helper(this: (QString *)"hw_id", a2: (const char *)5, a3: v11);
  55       QJsonObject::value(this: (QJsonObject *)v20, a2: (const QString *)&v19);
  56       QJsonValue::toString(this: (QJsonValue *)&v21);
     // ... excerpt omitted ...
  98   QJsonArray::~QJsonArray(this: (QJsonArray *)v25);
  99   return v14;
 100 }
```

## S9 Expiry

`0x10002d8c8`

```cpp
     // ... excerpt omitted ...
   1 __int64 __fastcall sub_10002D8C8(__int64 a1)
   2 {
   3   QDateTime *isNull; // x0
   4   __int64 v3; // x19
   5   __int64 v5; // [xsp+0h] [xbp-20h] BYREF
   6   __int64 v6; // [xsp+8h] [xbp-18h] BYREF
   7
   8   sub_100033A24(a1: &v6);
   9   if ( (QDateTime::isNull(this: (QDateTime *)&v6) & 1) != 0 )
  10     sub_100033BC8(a1: &v5, a2: a1);
  11   else
  12     QDateTime::QDateTime(this: (QDateTime *)&v5, a2: (const QDateTime *)&v6);
  13   QDateTime::~QDateTime(this: (QDateTime *)&v6);
  14   isNull = (QDateTime *)QDateTime::isNull(this: (QDateTime *)&v5);
  15   if ( ((unsigned __int8)isNull & 1) != 0 )
  16   {
  17     v3 = 0;
  18   }
  19   else
  20   {
  21     QDateTime::currentDateTime(this: isNull);
  22     v3 = QDateTime::operator<(this: (QDateTime *)&v5, a2: (const QDateTime *)&v6);
  23     QDateTime::~QDateTime(this: (QDateTime *)&v6);
  24   }
  25   QDateTime::~QDateTime(this: (QDateTime *)&v5);
  26   return v3;
  27 }
```

## S10 Main expiry field

`0x100033bc8`

```cpp
     // ... excerpt omitted ...
   1 void __usercall sub_100033BC8(__int64 a1@<X0>, int a2@<W2>, QDateTime *a3@<X8>)
   2 {
   3   int v5; // w2
     // ... excerpt omitted ...
  12
  13   v13 = (QArrayData *)QString::fromAscii_helper(this: (QString *)"main_period_ends_at", a2: (const char *)0x13, a3: a2);
  14   QDateTime::QDateTime(this: (QDateTime *)v11);
  15   sub_100033D6C(a1: &v12, a2: a1, a3: &v13, a4: v11);
  16   QDateTime::~QDateTime(this: (QDateTime *)v11);
  17   v7 = v13;
  18   if ( *(_DWORD *)v13 != -1 )
     // ... excerpt omitted ...
  28 LABEL_6:
  29   v13 = (QArrayData *)QString::fromAscii_helper(this: (QString *)"is_trial", a2: (const char *)8, a3: v5);
  30   v11[0] = 0;
  31   v9 = sub_1000134AC(a1, a2: &v13, a3: v11);
     // ... excerpt omitted ...
  45   {
  46     QDateTime::toTimeSpec(a1: &v12, a2: 1);
  47     QDateTime::setTimeSpec(a1: a3, a2: 0);
  48     QTime::QTime(this: (QTime *)&v13, a2: 23, a3: 59, a4: 59, a5: 0);
  49     QDateTime::setTime(this: a3, a2: (const QTime *)&v13);
  50   }
  51   else
  52   {
  53     QDateTime::QDateTime(this: a3, a2: (const QDateTime *)&v12);
  54   }
  55   QDateTime::~QDateTime(this: (QDateTime *)&v12);
  56 }
```

## S11 Grace expiry field

`0x100033a24`

```cpp
     // ... excerpt omitted ...
   1 void __usercall sub_100033A24(__int64 a1@<X0>, int a2@<W2>, QDateTime *a3@<X8>)
   2 {
   3   int v5; // w2
     // ... excerpt omitted ...
  12
  13   v13 = (QArrayData *)QString::fromAscii_helper(this: (QString *)"grace_period_ends_at", a2: (const char *)0x14, a3: a2);
  14   QDateTime::QDateTime(this: (QDateTime *)v11);
  15   sub_100033D6C(a1: &v12, a2: a1, a3: &v13, a4: v11);
  16   QDateTime::~QDateTime(this: (QDateTime *)v11);
  17   v7 = v13;
  18   if ( *(_DWORD *)v13 != -1 )
     // ... excerpt omitted ...
  28 LABEL_6:
  29   v13 = (QArrayData *)QString::fromAscii_helper(this: (QString *)"is_trial", a2: (const char *)8, a3: v5);
  30   v11[0] = 0;
  31   v9 = sub_1000134AC(a1, a2: &v13, a3: v11);
     // ... excerpt omitted ...
  45   {
  46     QDateTime::toTimeSpec(a1: &v12, a2: 1);
  47     QDateTime::setTimeSpec(a1: a3, a2: 0);
  48     QTime::QTime(this: (QTime *)&v13, a2: 23, a3: 59, a4: 59, a5: 0);
  49     QDateTime::setTime(this: a3, a2: (const QTime *)&v13);
  50   }
  51   else
  52   {
  53     QDateTime::QDateTime(this: a3, a2: (const QDateTime *)&v12);
  54   }
  55   QDateTime::~QDateTime(this: (QDateTime *)&v12);
  56 }
```

## S12 RSA verification

`0x10046245c`

```cpp
     // ... excerpt omitted ...
   1 __int64 __fastcall sub_10046245C(__int64 *a1, __int64 *a2)
   2 {
   3   __int64 v3; // x9
     // ... excerpt omitted ...
 102 LABEL_22:
 103   sub_100462A00(a1: v30, a2: v47);
 104   v48 = xmmword_1005AC000;
 105   v49 = xmmword_1005AC010;
 106   v50 = 0;
 107   v19 = *((char *)a1 + 23);
     // ... excerpt omitted ...
 115     v21 = a1[1];
 116   sub_100462C10(a1: &v48, a2: v20, a3: v21);
 117   v22 = vandq_s8(
 118           vandq_s8(vandq_s8(vandq_s8(v34, v38), vandq_s8(v36, v40)), vandq_s8(vandq_s8(v35, v39), vandq_s8(v37, v41))),
     // ... excerpt omitted ...
 135                                                                (int32x4_t)vceqq_s64(v31, v24),
 136                                                                (int32x4_t)vceqq_s64(v32, (int64x2_t)xmmword_1005ABDF0))));
 137   v25.i16[0] = vmaxv_u16(v25);
 138   if ( v30[0] == (HIDWORD(v49) | ((unsigned __int64)DWORD2(v49) << 32)) && v33 == -4291808976LL )
 139     v27 = (v30[1] == (DWORD1(v49) | ((unsigned __int64)(unsigned int)v49 << 32))) & ~v25.i32[0];
 140   else
 141     v27 = 0;
 142   if ( *(_QWORD *)&v23 == -1 && v46 == 0x1FFFFFFFFFFFFLL )
 143     return v27;
 144   else
 145     return 0;
 146 }
```

## S13 RSA exponentiation

`0x100462a00`

```cpp
     // ... excerpt omitted ...
  55   v3 = v53;
  56   v4 = sub_100462E58(a1: v53, a2: v52, a3: a2, a4: &unk_1005ABF00, a5: &unk_1005ABE00, a6: 0xA09E8BB4DFCDAF9LL);
  57   if ( v4 != 0 )
  58     v5 = v52;
     // ... excerpt omitted ...
  87   v16 = v51;
  88   v17 = 15;
  89   v51[12] = v13;
  90   v51[13] = v14;
     // ... excerpt omitted ...
  93     v18 = v3;
  94     if ( (unsigned int)sub_100462E58(a1: v3, a2: v16, a3: v16, a4: v16, a5: &unk_1005ABE00, a6: 0xA09E8BB4DFCDAF9LL) == 0 )
  95     {
  96       v3 = v16;
     // ... excerpt omitted ...
  98     }
  99     if ( ((1LL << v17) & 0x10001) != 0 )
 100     {
 101       v19 = sub_100462E58(a1: v3, a2: v16, a3: v16, a4: v5, a5: &unk_1005ABE00, a6: 0xA09E8BB4DFCDAF9LL);
 102       if ( v19 != 0 )
 103         v20 = v3;
     // ... excerpt omitted ...
 109     }
 110     --v17;
 111   }
 112   while ( v17 != -1 );
 113   v50 = 0;
 114   v49 = 0u;
     // ... excerpt omitted ...
 129   v34 = 1;
 130   if ( (unsigned int)sub_100462E58(a1: v3, a2: v16, a3: v16, a4: &v34, a5: &unk_1005ABE00, a6: 0xA09E8BB4DFCDAF9LL) != 0 )
 131     v21 = (__n128 *)v16;
 132   else
```

## S14 Host API headers

`0x100293c18`

```cpp
     // ... excerpt omitted ...
  28
  29   QByteArray::QByteArray(this: (QByteArray *)&v28, a2: "x-HostId", a3: -1);
  30   sub_10056A748(a1: &v26, a2: a1 + 192);
  31   QString::toUtf8_helper(this: &v26, a2: v4);
  32   QNetworkRequest::setRawHeader(this: a2, a2: (const QByteArray *)&v28, a3: (const QByteArray *)&v27);
  33   v6 = v27;
  34   if ( *(_DWORD *)v27 != -1 )
     // ... excerpt omitted ...
  68 LABEL_16:
  69   QByteArray::QByteArray(this: (QByteArray *)&v28, a2: "x-InstanceID", a3: -1);
  70   QNetworkRequest::setRawHeader(this: a2, a2: (const QByteArray *)&v28, a3: (const QByteArray *)(a1 + 216));
  71   v10 = (QArrayData *)v28;
  72   if ( *v28 != -1 )
     // ... excerpt omitted ...
  82 LABEL_21:
  83   QByteArray::QByteArray(this: (QByteArray *)&v27, a2: "Authorization", a3: -1);
  84   QByteArray::QByteArray(this: (QByteArray *)&v24, a2: "PrlHostBearer", a3: -1);
  85   v28 = (atomic_uint *)v24;
  86   if ( (unsigned int)(*(_DWORD *)v24 - 1) <= 0xFFFFFFFD )
     // ... excerpt omitted ...
 103 LABEL_30:
 104   sub_100294044(a1: &v23, a2: a1);
 105   v28 = (atomic_uint *)v25;
 106   if ( (unsigned int)(*(_DWORD *)v25 - 1) <= 0xFFFFFFFD )
     // ... excerpt omitted ...
 123 LABEL_39:
 124   QNetworkRequest::setRawHeader(this: a2, a2: (const QByteArray *)&v27, a3: (const QByteArray *)&v26);
 125   v18 = (QArrayData *)v26.var0;
 126   if ( *(_DWORD *)v26.var0 != -1 )
```

## S15 Host JWT

`0x100294044`

```cpp
     // ... excerpt omitted ...
  27   QArrayData *v26; // x0
  28   QDateTime *v27; // x0
  29   __int64 v28; // x0
  30   int v29; // w2
     // ... excerpt omitted ...
  49   QJsonObject::QJsonObject(this: (QJsonObject *)v46);
  50   QString::fromUtf8_helper(this: (QString *)"JWT", a2: (const char *)3, a3: v2);
  51   QJsonValue::QJsonValue(this: (QJsonValue *)v45, a2: &v43);
  52   var0 = (QArrayData *)v43.var0;
     // ... excerpt omitted ...
  63 LABEL_6:
  64   v40.var0 = (void *)QString::fromAscii_helper(this: (QString *)"typ", a2: (const char *)3, a3: v3);
  65   v43.var0 = (void *)QJsonObject::operator[](this: (QJsonObject *)v46, a2: &v40);
  66   v44 = v6;
     // ... excerpt omitted ...
  80   QJsonValue::~QJsonValue(this: (QJsonValue *)v45);
  81   QString::fromUtf8_helper(this: (QString *)"HS256", a2: (const char *)5, a3: v9);
  82   QJsonValue::QJsonValue(this: (QJsonValue *)v45, a2: &v43);
  83   v12 = (QArrayData *)v43.var0;
     // ... excerpt omitted ...
  94 LABEL_16:
  95   v40.var0 = (void *)QString::fromAscii_helper(this: (QString *)"alg", a2: (const char *)3, a3: v10);
  96   v43.var0 = (void *)QJsonObject::operator[](this: (QJsonObject *)v46, a2: &v40);
  97   v44 = v13;
     // ... excerpt omitted ...
 136   QJsonValue::QJsonValue(this: (QJsonValue *)v45, a2: &v40);
 137   v42.var0 = (void *)QString::fromAscii_helper(this: (QString *)"iss", a2: (const char *)3, a3: v21);
 138   v43.var0 = (void *)QJsonObject::operator[](this: (QJsonObject *)v46, a2: &v42);
 139   v44 = v22;
     // ... excerpt omitted ...
 166   v27 = QJsonObject::QJsonObject(this: (QJsonObject *)&v43);
 167   v28 = QDateTime::currentSecsSinceEpoch(this: v27);
 168   QJsonValue::QJsonValue(this: (QJsonValue *)v45, a2: v28 + 60);
 169   v42.var0 = (void *)QString::fromAscii_helper(this: (QString *)"exp", a2: (const char *)3, a3: v29);
 170   v40.var0 = (void *)QJsonObject::operator[](this: (QJsonObject *)&v43, a2: &v42);
 171   v41 = v30;
     // ... excerpt omitted ...
 187   QJsonValue::QJsonValue(this: (QJsonValue *)v45, a2: &v42);
 188   v39.var0 = (void *)QString::fromAscii_helper(this: (QString *)"sub", a2: (const char *)3, a3: v33);
 189   v40.var0 = (void *)QJsonObject::operator[](this: (QJsonObject *)&v43, a2: &v39);
 190   v41 = v34;
     // ... excerpt omitted ...
 220 LABEL_52:
 221   sub_1003F34C0(a1: a1 + 224, a2: v46, a3: &v43);
 222   QJsonObject::~QJsonObject(this: (QJsonObject *)&v43);
 223   QJsonObject::~QJsonObject(this: (QJsonObject *)v46);
```

## S16 HMAC encoding

`0x1003f34c0`

```cpp
     // ... excerpt omitted ...
  54   QJsonDocument::QJsonDocument(this: (QJsonDocument *)&v50, a2);
  55   QJsonDocument::toJson(a1: &v52, a2: &v50, a3: 1);
  56   QByteArray::toBase64(a1: &v51, a2: &v52, a3: 3);
  57   v8 = (QArrayData *)v52;
  58   if ( *v52 != -1 )
     // ... excerpt omitted ...
  70   QJsonDocument::QJsonDocument(this: (QJsonDocument *)v49, a2: a3);
  71   QJsonDocument::toJson(a1: &v52, a2: v49, a3: 1);
  72   QByteArray::toBase64(a1: &v50, a2: &v52, a3: 3);
  73   v10 = (QArrayData *)v52;
  74   if ( *v52 != -1 )
     // ... excerpt omitted ...
  86   v52 = (atomic_uint *)&QArrayData::shared_null;
  87   QMessageAuthenticationCode::QMessageAuthenticationCode(a1: v49, a2: 4, a3: &v52);
  88   v12 = (QArrayData *)v52;
  89   if ( *v52 != -1 )
     // ... excerpt omitted ...
  99 LABEL_16:
 100   QMessageAuthenticationCode::setKey(this: (QMessageAuthenticationCode *)v49, a2: a1);
 101   v52 = (atomic_uint *)v51;
 102   if ( (unsigned int)(*(_DWORD *)v51 - 1) <= 0xFFFFFFFD )
     // ... excerpt omitted ...
 138 LABEL_34:
 139   QMessageAuthenticationCode::addData(this: (QMessageAuthenticationCode *)v49, a2: (const QByteArray *)&v48);
 140   v20 = v48;
 141   if ( *(_DWORD *)v48 != -1 )
     // ... excerpt omitted ...
 163 LABEL_44:
 164   QMessageAuthenticationCode::result(this: (QMessageAuthenticationCode *)v49);
 165   QByteArray::toBase64(a1: &v48, a2: &v52, a3: 3);
 166   v23 = (QArrayData *)v52;
 167   if ( *v52 != -1 )
     // ... excerpt omitted ...
 302 LABEL_105:
 303   QMessageAuthenticationCode::~QMessageAuthenticationCode(this: (QMessageAuthenticationCode *)v49);
 304   v42 = v50;
 305   if ( *(_DWORD *)v50 == -1 )
```

## S17 API base construction

`0x1003f4558`

```cpp
     // ... excerpt omitted ...
  46       {
  47         case 0:
  48           v12 = (_DWORD *)QString::fromAscii_helper(this: (QString *)"https://desktop.%1", a2: (const char *)0x12, a3);
  49           v36.var0 = v12;
  50           v37.var0 = v12;
     // ... excerpt omitted ...
  52             atomic_fetch_add(v12, 1u);
  53           QString::fromUtf8_helper(this: (QString *)"/account", a2: (const char *)8, a3: v13);
  54           QString::append(this: &v37, a2: &v38);
  55           var0 = (QArrayData *)v38.var0;
     // ... excerpt omitted ...
  82           goto LABEL_82;
  83         case 1:
  84           v22 = (_DWORD *)QString::fromAscii_helper(this: (QString *)"https://desktop.%1", a2: (const char *)0x12, a3);
  85           v36.var0 = v22;
  86           v37.var0 = v22;
     // ... excerpt omitted ...
  88             atomic_fetch_add(v22, 1u);
  89           QString::fromUtf8_helper(this: (QString *)"/access", a2: (const char *)7, a3: v23);
  90           QString::append(this: &v37, a2: &v38);
  91           v25 = (QArrayData *)v38.var0;
     // ... excerpt omitted ...
 118           goto LABEL_82;
 119         case 2:
 120           QString::fromUtf8_helper(this: (QString *)"https://access.%1/license/api/v1", a2: (const char *)0x20, a3);
 121           goto LABEL_102;
 122         default:
     // ... excerpt omitted ...
 125     }
 126     if ( a1 == 3 )
 127     {
 128       QString::fromUtf8_helper(this: (QString *)"https://static.parallels.com/i", a2: (const char *)0x1E, a3);
 129       goto LABEL_102;
 130     }
 131     if ( a1 == 4 )
 132     {
 133       QString::fromUtf8_helper(this: (QString *)"https://access.%1/agent_api/v1", a2: (const char *)0x1E, a3);
 134       goto LABEL_102;
 135     }
 136     v10 = (_DWORD *)QString::fromAscii_helper(this: (QString *)"https://desktop.%1", a2: (const char *)0x12, a3);
 137     v36.var0 = v10;
 138     v37.var0 = v10;
     // ... excerpt omitted ...
 140       atomic_fetch_add(v10, 1u);
 141     QString::fromUtf8_helper(this: (QString *)"/api/v1", a2: (const char *)7, a3: v11);
 142     QString::append(this: &v36, a2: &v38);
 143 LABEL_52:
     // ... excerpt omitted ...
 184     {
 185       case 9:
 186         QString::fromUtf8_helper(this: (QString *)"https://account.%1/api/v1/webinstaller", a2: (const char *)0x26, a3);
 187         break;
 188       case 10:
 189         QString::fromUtf8_helper(this: (QString *)"https://reportus.%1/api", a2: (const char *)0x17, a3);
 190         break;
 191       case 11:
 192         QString::fromUtf8_helper(this: (QString *)"https://pda-api.%1/api", a2: (const char *)0x16, a3);
 193         break;
 194       default:
     // ... excerpt omitted ...
 210   }
 211   if ( a1 == 6 )
 212   {
 213     v17 = (_DWORD *)QString::fromAscii_helper(this: (QString *)"https://desktop.%1", a2: (const char *)0x12, a3);
 214     v36.var0 = v17;
 215     v37.var0 = v17;
     // ... excerpt omitted ...
 217       atomic_fetch_add(v17, 1u);
 218     QString::fromUtf8_helper(this: (QString *)"/dispatcher_api/v1", a2: (const char *)0x12, a3: v18);
 219     QString::append(this: &v36, a2: &v38);
 220     goto LABEL_52;
 221   }
 222   if ( a1 != 7 )
 223   {
 224     v4 = (_DWORD *)QString::fromAscii_helper(this: (QString *)"https://desktop.%1", a2: (const char *)0x12, a3);
 225     v36.var0 = v4;
 226     v37.var0 = v4;
     // ... excerpt omitted ...
 228       atomic_fetch_add(v4, 1u);
 229     QString::fromUtf8_helper(this: (QString *)"/license", a2: (const char *)8, a3: v5);
 230     QString::append(this: &v37, a2: &v38);
 231     v8 = (QArrayData *)v38.var0;
     // ... excerpt omitted ...
 258 LABEL_82:
 259     QString::fromUtf8_helper(this: (QString *)"/api/v1", a2: (const char *)7, a3: v6);
 260     QString::append(this: &v34, a2: &v38);
 261     v27 = (QArrayData *)v38.var0;
     // ... excerpt omitted ...
 298   }
 299   v30 = (QArrayData *)QString::fromAscii_helper(this: (QString *)"https://kb.parallels.com", a2: (const char *)0x18, a3);
 300   v21 = v35;
 301   v35 = v30;
```

## S18 VM startup gate

`0x100057ca4`

```cpp
     // ... excerpt omitted ...
 317                   a4: 0,
 318                   a5: "Start VM: %s, uuid=%s cannot be done as x86 Emulation is supported only on Professional and Business license",
 319                   (const char *)&v90,
 320                   (const char *)&v89);
     // ... excerpt omitted ...
 581     sub_100025788(a1: &v93, a2: qword_1007225C8);
 582     if ( (unsigned int)sub_100279B3C(a1: *((_QWORD *)v93 + 1) + 48LL) == 0 )
 583     {
 584       v42 = v94;
     // ... excerpt omitted ...
 591     }
 592     v23 = sub_100279B3C(a1: *((_QWORD *)v93 + 1) + 48LL);
 593     v24 = v23;
 594     v25 = *((atomic_uint **)*a1 + 1);
 595     v98 = v25;
     // ... excerpt omitted ...
 603       a4: 0,
 604       a5: "Failed to start VM %s: license status %#x (%s)",
 605       (const char *)&v98,
 606       v24,
```

## S19 Heartbeat state machine

`0x1001575dc`

```cpp
     // ... excerpt omitted ...
   1 void __fastcall sub_1001575DC(__int64 a1, int a2)
   2 {
   3   __int64 v4; // x0
     // ... excerpt omitted ...
  28   {
  29     sub_1001580A0(result: a1, a2);
  30     return;
  31   }
     // ... excerpt omitted ...
  33   {
  34     sub_1001580A0(result: a1, a2: a2 & 0xFFFFFFFB);
  35     return;
  36   }
     // ... excerpt omitted ...
  38   {
  39     v5 = sub_1005756CC(a1: "", a2: "disp", a3: 0, a4: "Cleanup storage by flags");
  40     v4 = sub_10015698C(a1: v5);
  41   }
  42   sub_100157938(a1: v4, a2: (a2 & 8) != 0, a3: (QDateTime *)v25);
  43   if ( (a2 & 2) != 0 )
  44     v6 = sub_100157A24();
  45   else
  46     v6 = 0;
     // ... excerpt omitted ...
  51     QDateTime::QDateTime(this: (QDateTime *)&v19, a2: (const QDateTime *)&v24);
  52     v13 = sub_10015813C(a1, a2: &v19, a3: v6);
  53     QDateTime::~QDateTime(this: (QDateTime *)&v19);
  54     if ( v13 != 0 )
  55     {
  56       sub_1001581D8(a1: &v19);
  57       if ( v19 != nullptr )
  58       {
  59         sub_1001582B4(a1, a2: &v19);
  60         goto LABEL_36;
  61       }
     // ... excerpt omitted ...
  64     {
  65       if ( (unsigned int)sub_100158418(a1, a2: v25, a3: v6) == 0 )
  66       {
  67         QDateTime::QDateTime(this: (QDateTime *)&v19, a2: (const QDateTime *)&v24);
  68         sub_100158604(this: (QObject *)a1);
  69         QDateTime::~QDateTime(this: (QDateTime *)&v19);
  70         goto LABEL_39;
  71       }
  72       sub_1001581D8(a1: &v19);
  73       if ( v19 != nullptr )
  74       {
  75         sub_1001584A0(a1, a2: &v19);
  76         goto LABEL_36;
  77       }
  78     }
  79     sub_1001580A0(result: a1, a2);
  80 LABEL_36:
  81     v16 = v20;
```

## S20 Heartbeat scheduling

`0x100158884`

```cpp
     // ... excerpt omitted ...
   1 void __usercall sub_100158884(QDateTime *__return_ptr a1@<X8>, QDateTime *this@<X1>, char a3@<W2>)
   2 {
   3   QDateTime *isNull; // x0
   4   __int64 v7; // x0
   5   __int64 v8; // x0
     // ... excerpt omitted ...
  10
  11   isNull = (QDateTime *)QDateTime::isNull(this);
  12   v7 = QDateTime::currentDateTime(this: isNull);
  13   v8 = sub_100156C90(a1: v7);
  14   sub_1001502E0(a1: &v11, a2: v8);
  15   QDateTime::QDateTime(this: a1);
  16   if ( (unsigned int)QDateTime::operator<(this: (QDateTime *)v12, a2: this) == 0 )
  17   {
  18     if ( (__int64)QDateTime::secsTo(this, a2: (const QDateTime *)v12) <= 604799 )
  19     {
  20       QDateTime::addSecs(this, a2: 604800);
  21 LABEL_5:
  22       v9 = *(_QWORD *)a1;
     // ... excerpt omitted ...
  24       v10 = v9;
  25       QDateTime::~QDateTime(this: (QDateTime *)&v10);
  26       goto LABEL_6;
  27     }
  28     if ( (a3 & 1) == 0
  29       && (QDateTime::isNull(this: (QDateTime *)&v11) & 1) == 0
  30       && (__int64)QDateTime::secsTo(this: (QDateTime *)&v11, a2: (const QDateTime *)v12) <= 86400
  31       && (unsigned int)QDateTime::operator<(this: (QDateTime *)v12, a2: (const QDateTime *)&v11) == 0 )
  32     {
  33       QDateTime::addSecs(this: (QDateTime *)&v11, a2: 86400);
  34       goto LABEL_5;
  35     }
  36   }
  37   QDateTime::operator=(this: a1, a2: (const QDateTime *)v12);
  38 LABEL_6:
  39   QDateTime::~QDateTime(this: (QDateTime *)&v11);
  40   QDateTime::~QDateTime(this: (QDateTime *)v12);
  41 }
```

## S21 Renewal scheduling

`0x100158728`

```cpp
     // ... excerpt omitted ...
   1 void __usercall sub_100158728(QDateTime *__return_ptr a1@<X8>, QDateTime *this@<X1>, char a3@<W2>)
   2 {
   3   QDateTime *isNull; // x0
   4   __int64 v7; // x0
   5   __int64 v8; // x0
     // ... excerpt omitted ...
  11
  12   isNull = (QDateTime *)QDateTime::isNull(this);
  13   if ( (_DWORD)isNull != 0 )
  14   {
  15     QDateTime::QDateTime(this: a1);
  16     return;
  17   }
  18   v7 = QDateTime::currentDateTime(this: isNull);
  19   v8 = sub_100156D3C(a1: v7);
  20   sub_1001502E0(a1: &v12, a2: v8);
  21   QDateTime::QDateTime(this: a1);
  22   v9 = QDateTime::secsTo(this: (QDateTime *)v13, a2: this);
  23   if ( v9 < 1 )
  24   {
  25     if ( (a3 & 1) != 0
  26       || (QDateTime::isNull(this: (QDateTime *)&v12) & 1) != 0
  27       || (__int64)QDateTime::secsTo(this: (QDateTime *)&v12, a2: (const QDateTime *)v13) > 86400
  28       || (unsigned int)QDateTime::operator<(this: (QDateTime *)v13, a2: (const QDateTime *)&v12) != 0 )
  29     {
  30       QDateTime::operator=(this: a1, a2: (const QDateTime *)v13);
  31       goto LABEL_11;
  32     }
  33     QDateTime::addSecs(this: (QDateTime *)&v12, a2: 86400);
  34   }
  35   else
  36   {
  37     QDateTime::addSecs(this: (QDateTime *)v13, a2: v9 & 0x7FFFFFFF);
  38   }
  39   v10 = *(_QWORD *)a1;
     // ... excerpt omitted ...
  41   v11 = v10;
  42   QDateTime::~QDateTime(this: (QDateTime *)&v11);
  43 LABEL_11:
  44   QDateTime::~QDateTime(this: (QDateTime *)&v12);
  45   QDateTime::~QDateTime(this: (QDateTime *)v13);
  46 }
```

## S22 Heartbeat result

`0x100158c28`

```cpp
     // ... excerpt omitted ...
   4   const char *v4; // x0
   5   QDateTime *v5; // x0
   6   __int64 v6; // x0
   7   int v7; // w0
     // ... excerpt omitted ...
  14   v4 = (const char *)sub_10056E3B4(a1: a2);
  15   v5 = (QDateTime *)sub_1005756CC(
  16                       a1: "",
  17                       a2: "disp",
  18                       a3: 0,
  19                       a4: "Heartbeat call has finished with result %#x, %s",
  20                       v2,
  21                       v4);
  22   v6 = QDateTime::currentDateTime(this: v5);
  23   v7 = sub_100156C90(a1: v6);
  24   v8 = sub_1001503D4(a1: v7, this: (QDateTime *)v11);
  25   if ( (v8 & 1) == 0 )
  26     v8 = sub_1005756CC(a1: "", a2: "disp", a3: 0, a4: "Unable to store last heartbeat attempt datetime.");
  27   if ( (v2 & 0x80000000) == 0 || v2 == -47024 || v2 == -47031 )
  28   {
  29     v9 = sub_100156BE4(a1: v8);
  30     if ( (sub_1001503D4(a1: v9, this: (QDateTime *)v11) & 1) == 0 )
  31       sub_1005756CC(a1: "", a2: "disp", a3: 0, a4: "Unable to store last heartbeat datetime.");
  32   }
     // ... excerpt omitted ...
  35   *(_QWORD *)(a1 + 40) = 0;
  36   if ( v10 != nullptr && atomic_fetch_add(&v10->__shared_owners_, 0xFFFFFFFFFFFFFFFFLL) == 0 )
  37   {
  38     ((void (__fastcall *)(std::__shared_weak_count *))v10->__on_zero_shared)(a1: v10);
     // ... excerpt omitted ...
  41   sub_1001580A0(a1, a2: 0);
  42   QDateTime::~QDateTime(this: (QDateTime *)v11);
  43 }
```

## S23 Offline sign out

`0x10014f32c`

```cpp
     // ... excerpt omitted ...
  37       a3: 0,
  38       a4: "Failed to sign out offline. Another license operation is already running.");
  39     result = 4294956256LL;
  40     v12 = v19;
     // ... excerpt omitted ...
  44   }
  45   v2 = sub_1001507D0(a1: v0);
  46   if ( v2 == -14 )
  47     v3 = 0;
     // ... excerpt omitted ...
  50   sub_100025788(a1: &v16, a2: qword_1007225C8);
  51   v4 = sub_10027A3F8(a1: *(_QWORD *)(v16 + 8) + 48LL);
  52   v5 = sub_10027A208(a1: *(_QWORD *)(v16 + 8) + 48LL);
  53   v6 = (const char *)sub_10056E3B4(a1: v3);
  54   v7 = (const char *)sub_10056E3B4(a1: v4);
     // ... excerpt omitted ...
  59     a3: 0,
  60     a4: "Offline sign out operation has finished with results: cleanup tokens %s,  cleanup pubKey %s, cleanup license %s",
  61     v6,
  62     v7,
```

## S24 License path

`0x100513620`

```cpp
     // ... excerpt omitted ...
  10
  11   sub_1005130F4(a1: &v7);
  12   v3 = v7;
  13   a1->var0 = v7;
     // ... excerpt omitted ...
  15     atomic_fetch_add((atomic_uint *volatile)v3, 1u);
  16   QString::fromUtf8_helper(this: (QString *)"/licenses.json", a2: (const char *)0xE, a3: v2);
  17   QString::append(this: a1, a2: &v8);
  18   var0 = (QArrayData *)v8.var0;
```

## S25 Config directory

`0x1005130f4`

```cpp
     // ... excerpt omitted ...
  24   a2->var0 = &QArrayData::shared_null;
  25   v21 = (QArrayData *)QString::fromAscii_helper(this: (QString *)"PARALLELS_CONFIG_DIR", a2: (const char *)0x14, a3: a1);
  26   sub_10056AB20(a1: &v22, a2: &v21);
  27   var0 = a2->var0;
     // ... excerpt omitted ...
  55   {
  56     QString::fromUtf8_helper(this: (QString *)"/Library/Preferences", a2: (const char *)0x14, a3: v3);
  57     v12 = a2->var0;
  58     a2->var0 = v22.var0;
     // ... excerpt omitted ...
  84 LABEL_28:
  85     QString::fromUtf8_helper(this: (QString *)"Parallels", a2: (const char *)9, a3: v13);
  86     QString::normalized(a1: &v22, a2: &v21, a3: 1, a4: 0);
  87     QString::append(this: a2, a2: &v22);
```

## S26 Service token request

`0x10016028c`

```cpp
     // ... excerpt omitted ...
  51   }
  52   v3 = sub_1001506D0(a1: v2);
  53   sub_10014FEEC(a1: &v40, a2: v3);
  54   if ( *((_DWORD *)v40.var0 + 1) == 0 )
     // ... excerpt omitted ...
  87   v33 = (QArrayData *)QString::fromAscii_helper(this: (QString *)off_10071DB80[0], a2: (const char *)v10, a3: v7);
  88   v38.var0 = (void *)QString::fromAscii_helper(this: (QString *)"gen_auth_token", a2: (const char *)0xE, a3: v11);
  89   QVariant::QVariant(this: (QVariant *)&__p, a2: &v38);
  90   sub_10014D6A8(a1: (int)&v39, a2: (QString *)&v33);
     // ... excerpt omitted ...
 143   {
 144     v23 = off_10071DC28[0];
 145     if ( off_10071DC28[0] != nullptr )
 146       goto LABEL_40;
 147     goto LABEL_42;
     // ... excerpt omitted ...
 150   {
 151     v23 = off_10071DC20[0];
 152     if ( off_10071DC20[0] != nullptr )
 153     {
 154 LABEL_40:
     // ... excerpt omitted ...
 198   v38.var0 = (void *)QString::fromAscii_helper(
 199                        this: (QString *)"1onGetServiceToken(PRL_RESULT, const QVariant&)",
 200                        a2: (const char *)0x2F,
 201                        a3: v26);
```

## S27 Verified constants

RSA modulus at 0x1005ABE00 is 2048 bits. The exponentiation loop uses exponent 0x10001 (65537). Hash initial words at 0x1005AC000 and 0x1005AC010 are the SHA256 initial state. The PKCS1 comparison includes the SHA256 DigestInfo prefix and FF padding.

Operation table at 0x1006BD168, indexed by operation plus one: operation 2 heartbeat, 3 deactivate, 4 activate, 5 get_trial, 6 activate, 9 sso_activate.

Resolved parameter pointers in account builder: 0x10071DB98 email; 0x10071DBA0 password; 0x10071DC30 service; 0x10071DC38 fb; 0x10071DC40 gp; 0x10071DC48 token; 0x10071DC50 prl_app_id; 0x10071DC58 code; 0x10071DC60 sign_in_through_web. Service token builder: 0x10071DC20 lic; 0x10071DC28 self. Stored license keys: 0x1006EF6D0 license; 0x1006EF6D8 signature; 0x1006EF6E0 publicCerts.

Disassembly of 0x100293AC0 passes W0=11 to API base builder 0x1003F4558. This takes the default license API branch. The legacy payload builder sets location 6; account authentication sets location 0.

## GUI evidence

libPrlGui.3.dylib ARM64 slice, image base 0. Full universal file SHA256 dbb60747b2d793214af2096b392dfa08bd11758cf9a76092187acf3823929e45. Addresses are slice virtual addresses.

## G1 GUI sign in handoff

`0xe8bdc`

```cpp
     // ... excerpt omitted ...
  85   {
  86     case 0:
  87       QString::fromUtf8_helper(
  88         this: (QString *)"{2CD98450-E2A1-4018-95A7-C1873C6C3052}",
     // ... excerpt omitted ...
 111       goto LABEL_51;
 112     case 1:
 113       QString::fromUtf8_helper(
 114         this: (QString *)"{B6194A3A-AC31-4E79-ADEE-92D18E22AEE5}",
     // ... excerpt omitted ...
 155       SdkUtils::makeStringsList(a1: &v45, a2: &v49);
 156       v48 = PrlSrv_StoreValueByKey(a1: v23, a2: (char *)v25 + v26, a3: v45, a4: 0);
 157       CRequestInfo::CRequestInfo(this: (CRequestInfo *)&v41, a2: 0x852u, a3: nullptr);
 158       v27 = CSdkCommunicator::createRequest(a1: v21, a2: &v48, a3: &v41);
 159       QVariant::~QVariant(this: (QVariant *)&v44);
 160       if ( __p != nullptr && atomic_fetch_add((atomic_uint *volatile)__p, 0xFFFFFFFF) == 1 && __p != nullptr )
     // ... excerpt omitted ...
 253       return v27;
 254     case 2:
 255       QString::fromUtf8_helper(
 256         this: (QString *)"{0DD7E65E-0FD2-4063-BC62-3339144A381B}",
     // ... excerpt omitted ...
 271       goto LABEL_50;
 272     case 3:
 273       QString::fromUtf8_helper(
 274         this: (QString *)"{D5C16C3E-A192-4259-9C19-13C302AFE620}",
     // ... excerpt omitted ...
 321     default:
 322       sub_1F43AC(a1: "", a2: "PrlGui", a3: 0, a4: "Unknown auth type: %d.", *(_DWORD *)(a1 + 64));
 323       goto LABEL_52;
 324   }
```

## G2 Google authorization URL

`0xefc64`

```cpp
     // ... excerpt omitted ...
   2 {
   3   CWebAuthHttpServer *v2; // x20
   4   int v3; // w2
   5   const QObject *v4; // x1
     // ... excerpt omitted ...
  13   __int64 v12; // x8
  14   QTcpServer *v13; // x20
  15   int v14; // w2
  16   __int64 v15; // x8
  17   QTcpServer *v16; // x0
  18   unsigned int v17; // w0
  19   unsigned __int64 v18; // x3
     // ... excerpt omitted ...
  53
  54   v2 = (CWebAuthHttpServer *)operator new(__sz: 0x18u);
  55   v50[0] = (QArrayData *)QString::fromAscii_helper(
  56                            this: (QString *)"https://google.com",
  57                            a2: (const char *)&_mh_dylib_header.ncmds + 2,
  58                            a3: v3);
  59   QUrl::QUrl(a1: &Uuid, a2: v50, a3: 0);
  60   CWebAuthHttpServer::CWebAuthHttpServer(this: v2, a2: (const QUrl *)&Uuid, a3: (QObject *)this);
  61   v5 = QtSharedPointer::ExternalRefCountData::getAndRef(this: v2, a2: v4);
  62   v6 = *((void **)this + 10);
     // ... excerpt omitted ...
  88     v10 = 0;
  89   Uuid = (QArrayData *)CWebAuthHttpServer::authorizationFinished;
  90   v52 = 0;
  91   v50[0] = (QArrayData *)CTaskGoogleLogin::onGetAuthCodeFinished;
     // ... excerpt omitted ...
 106     a8: 0,
 107     a9: &CWebAuthHttpServer::staticMetaObject);
 108   if ( v49.d != nullptr )
 109     QMetaObject::Connection::isConnected_helper(this: (QMetaObject::Connection *)&v49);
     // ... excerpt omitted ...
 112   if ( v12 != 0 && *(_DWORD *)(v12 + 4) != 0 )
 113     v13 = *((QTcpServer **)this + 11);
 114   else
 115     v13 = nullptr;
 116   QHostAddress::QHostAddress(a1: &Uuid, a2: 4);
 117   QTcpServer::listen(this: v13, a2: (const QHostAddress *)&Uuid, a3: 0);
 118   QHostAddress::~QHostAddress(this: (QHostAddress *)&Uuid);
 119   v50[0] = (QArrayData *)QString::fromAscii_helper(
 120                            this: (QString *)"http://127.0.0.1:%1/",
 121                            a2: (const char *)&_mh_dylib_header.sizeofcmds,
 122                            a3: v14);
     // ... excerpt omitted ...
 124   if ( v15 != 0 && *(_DWORD *)(v15 + 4) != 0 )
 125     v16 = *((QTcpServer **)this + 11);
 126   else
 127     v16 = nullptr;
 128   v17 = QTcpServer::serverPort(this: v16);
 129   QString::arg(a1: &Uuid, a2: v50, a3: v17, a4: 0, a5: 10, a6: 32);
 130   v19 = *((QArrayData **)this + 3);
     // ... excerpt omitted ...
 159 LABEL_33:
 160   Uuid = (QArrayData *)QUuid::createUuid(this: v20);
 161   v52 = v21;
 162   QUuid::toString(a1: v50, a2: &Uuid, a3: 3);
 163   v24 = *((QArrayData **)this + 7);
 164   *((QArrayData **)this + 7) = v50[0];
     // ... excerpt omitted ...
 177   v50[0] = (QArrayData *)QString::fromAscii_helper(
 178                            this: (QString *)"https://accounts.google.com/o/oauth2/v2/auth",
 179                            a2: &stru_20.segname[4],
 180                            a3: v22);
     // ... excerpt omitted ...
 195   v49.d = (void *)QString::fromAscii_helper(
 196                     this: (QString *)"client_id",
 197                     a2: (const char *)&_mh_dylib_header.cpusubtype + 1,
 198                     a3: v27);
     // ... excerpt omitted ...
 212   v49.d = (void *)QString::fromAscii_helper(
 213                     this: (QString *)"redirect_uri",
 214                     a2: (const char *)&_mh_dylib_header.filetype,
 215                     a3: v28);
     // ... excerpt omitted ...
 229   v49.d = (void *)QString::fromAscii_helper(
 230                     this: (QString *)"response_type",
 231                     a2: (const char *)&_mh_dylib_header.filetype + 1,
 232                     a3: v31);
 233   v48.d = (void *)QString::fromAscii_helper(
 234                     this: (QString *)"code",
 235                     a2: (const char *)&_mh_dylib_header.cputype,
 236                     a3: v34);
     // ... excerpt omitted ...
 262   v49.d = (void *)QString::fromAscii_helper(
 263                     this: (QString *)"scope",
 264                     a2: (const char *)&_mh_dylib_header.cputype + 1,
 265                     a3: v35);
 266   v48.d = (void *)QString::fromAscii_helper(
 267                     this: (QString *)"openid profile email",
 268                     a2: (const char *)&_mh_dylib_header.sizeofcmds,
 269                     a3: v39);
     // ... excerpt omitted ...
 295   v49.d = (void *)QString::fromAscii_helper(
 296                     this: (QString *)"state",
 297                     a2: (const char *)&_mh_dylib_header.cputype + 1,
 298                     a3: v40);
     // ... excerpt omitted ...
 316   QUrl::setQuery(this: (QUrl *)&Uuid, a2: (const QUrlQuery *)v50);
 317   SystemUtils::openUrl(this: (SystemUtils *)&Uuid, a2: v46);
 318   CTaskGoogleLogin::webAuthStarted(this);
 319   CAbstractTask::setWaitForSubTaskCompletion(this);
```

## G3 Google callback state check

`0xf0344`

```cpp
     // ... excerpt omitted ...
  40     v6 = d[1] != 0 ? (QTcpServer *)a1[11].d : nullptr;
  41     QTcpServer::close(this: v6);
  42     v7 = a1[10].d;
  43     if ( v7 != nullptr && v7[1] != 0 )
     // ... excerpt omitted ...
  50   v34 = (QArrayData *)QString::fromAscii_helper(
  51                         this: (QString *)"code",
  52                         a2: (const char *)&_mh_dylib_header.cputype,
  53                         a3);
     // ... excerpt omitted ...
  69       {
  70         v15 = operator==(a1: (const QString *)&v34, a2: v13 + 2);
  71         v13 = (const QString *)v12->d;
  72         v9 = *a2;
     // ... excerpt omitted ...
 123   v34 = (QArrayData *)QString::fromAscii_helper(
 124                         this: (QString *)"state",
 125                         a2: (const char *)&_mh_dylib_header.cputype + 1,
 126                         a3: v18);
     // ... excerpt omitted ...
 142       {
 143         v27 = operator==(a1: (const QString *)&v34, a2: v25 + 2);
 144         v25 = (const QString *)v24->d;
 145         v21 = *a2;
     // ... excerpt omitted ...
 177 LABEL_46:
 178   v30 = operator==(a1: &v37, a2: a1 + 7);
 179   v31 = 4294967021LL;
 180   if ( (v30 & 1) != 0 )
 181   {
 182     if ( *((_DWORD *)a1[4].d + 1) != 0 )
 183       v31 = 0;
 184     else
 185       v31 = 4294967021LL;
 186   }
 187   (*((void (__fastcall **)(QString *, __int64))a1->d + 22))(a1, a2: v31);
 188   CTaskGoogleLogin::webAuthFinished(this: (CTaskGoogleLogin *)a1);
 189   result = (QArrayData *)v37.d;
```

## G4 Google token exchange

`0xf06a4`

```cpp
     // ... excerpt omitted ...
  37
  38   QNetworkRequest::QNetworkRequest(this: (QNetworkRequest *)v36);
  39   v34 = (QArrayData *)QString::fromAscii_helper(
  40                         this: (QString *)"https://www.googleapis.com/oauth2/v4/token",
  41                         a2: &stru_20.segname[2],
  42                         a3: v2);
     // ... excerpt omitted ...
  55 LABEL_6:
  56   QNetworkRequest::setUrl(this: (QNetworkRequest *)v36, a2: (const QUrl *)v35);
  57   QByteArray::QByteArray(this: (QByteArray *)&v34, a2: "Content-Type", a3: -1);
  58   QByteArray::QByteArray(this: (QByteArray *)&v33, a2: "application/x-www-form-urlencoded", a3: -1);
  59   QNetworkRequest::setRawHeader(
  60     this: (QNetworkRequest *)v36,
  61     a2: (const QByteArray *)&v34,
  62     a3: (const QByteArray *)&v33);
     // ... excerpt omitted ...
  88   v33.d = (void *)QString::fromAscii_helper(
  89                     this: (QString *)"client_id",
  90                     a2: (const char *)&_mh_dylib_header.cpusubtype + 1,
  91                     a3: v8);
     // ... excerpt omitted ...
 105   v33.d = (void *)QString::fromAscii_helper(
 106                     this: (QString *)"redirect_uri",
 107                     a2: (const char *)&_mh_dylib_header.filetype,
 108                     a3: v9);
     // ... excerpt omitted ...
 122   v33.d = (void *)QString::fromAscii_helper(
 123                     this: (QString *)"client_secret",
 124                     a2: (const char *)&_mh_dylib_header.filetype + 1,
 125                     a3: v12);
     // ... excerpt omitted ...
 139   v33.d = (void *)QString::fromAscii_helper(
 140                     this: (QString *)"grant_type",
 141                     a2: (const char *)&_mh_dylib_header.cpusubtype + 2,
 142                     a3: v15);
 143   v32.d = (void *)QString::fromAscii_helper(
 144                     this: (QString *)"authorization_code",
 145                     a2: (const char *)&_mh_dylib_header.ncmds + 2,
 146                     a3: v18);
     // ... excerpt omitted ...
 172   v33.d = (void *)QString::fromAscii_helper(
 173                     this: (QString *)"code",
 174                     a2: (const char *)&_mh_dylib_header.cputype,
 175                     a3: v19);
     // ... excerpt omitted ...
 202 LABEL_51:
 203   v28 = QNetworkAccessManager::post(
 204           this: *((QNetworkAccessManager **)this + 12),
 205           a2: (const QNetworkRequest *)v36,
 206           a3: (const QByteArray *)&v33);
 207   QObject::connect(a1: &v32, a2: v28, a3: "2finished()", a4: this, a5: "1onGetAuthTokenFinished()", a6: 0);
     // ... excerpt omitted ...
 229   QUrl::~QUrl(this: (QUrl *)v35);
 230   QNetworkRequest::~QNetworkRequest(this: (QNetworkRequest *)v36);
 231   return 0;
 232 }
```

## G5 Social token persistence

`0xe3fc8`

```cpp
     // ... excerpt omitted ...
  12
  13   if ( a2 == 2 )
  14   {
  15     QSettings::QSettings(this: (QSettings *)v12, a2: nullptr);
  16     v9 = (QArrayData *)QString::fromAscii_helper(this: (QString *)"", a2: nullptr, a3: v5);
  17     sub_1590D8(a1: &v10, a2: &v9, a3);
  18     QVariant::QVariant(this: (QVariant *)v11, a2: &v10);
  19     QSettings::setValue(this: (QSettings *)v12, a2: (const QString *)&qword_3ADBC8, a3: (const QVariant *)v11);
  20   }
  21   else
  22   {
  23     if ( a2 != 1 )
  24       return;
  25     QSettings::QSettings(this: (QSettings *)v12, a2: nullptr);
  26     v9 = (QArrayData *)QString::fromAscii_helper(this: (QString *)"", a2: nullptr, a3: v4);
  27     sub_1590D8(a1: &v10, a2: &v9, a3);
  28     QVariant::QVariant(this: (QVariant *)v11, a2: &v10);
  29     QSettings::setValue(this: (QSettings *)v12, a2: (const QString *)&qword_3ADBC0, a3: (const QVariant *)v11);
  30   }
  31   QVariant::~QVariant(this: (QVariant *)v11);
     // ... excerpt omitted ...
  59 LABEL_15:
  60   QSettings::~QSettings(this: (QSettings *)v12);
  61 }
```

## G6 Social token retrieval

`0xe3dc0`

```cpp
     // ... excerpt omitted ...
  19   v15 = (QArrayData *)&QArrayData::shared_null;
  20   if ( a1 == 2 )
  21   {
  22     QSettings::QSettings(this: (QSettings *)v12, a2: nullptr);
  23     v11 = 0x80000000;
  24     v10 = 0;
  25     QSettings::value(this: (QSettings *)v12, a2: (const QString *)&qword_3ADBC8, a3: (const QVariant *)&v10);
  26     QVariant::toString(this: (QVariant *)v13);
  27   }
     // ... excerpt omitted ...
  29   {
  30     if ( a1 != 1 )
  31       goto LABEL_11;
  32     QSettings::QSettings(this: (QSettings *)v12, a2: nullptr);
  33     v11 = 0x80000000;
  34     v10 = 0;
  35     QSettings::value(this: (QSettings *)v12, a2: (const QString *)&qword_3ADBC0, a3: (const QVariant *)&v10);
  36     QVariant::toString(this: (QVariant *)v13);
  37   }
     // ... excerpt omitted ...
  58   QVariant::~QVariant(this: (QVariant *)&v10);
  59   QSettings::~QSettings(this: (QSettings *)v12);
  60 LABEL_11:
  61   result = (atomic_uint *)v15;
     // ... excerpt omitted ...
  64     v13[0] = (QArrayData *)QString::fromAscii_helper(this: (QString *)"", a2: nullptr, a3: a2);
  65     sub_1595C0(a1: v13, a2: &v15);
  66     v9 = v13[0];
  67     if ( *(_DWORD *)v13[0] != -1 )
```

## G7 Social token encryption

`0x1590d8`

```cpp
     // ... excerpt omitted ...
   5   __int64 v6; // x9
   6   _CCCryptor *v7; // x20
   7   QArrayData *v8; // x23
   8   __int64 v9; // x24
     // ... excerpt omitted ...
  12   QArrayData *v13; // x8
  13   _CCCryptor *v14; // x20
  14   __int64 v15; // x9
  15   unsigned __int64 v16; // x3
     // ... excerpt omitted ...
  26   size_t dataOutMoved; // [xsp+28h] [xbp-58h] BYREF
  27   CCCryptorRef cryptorRef; // [xsp+30h] [xbp-50h] BYREF
  28   QArrayData *v29; // [xsp+38h] [xbp-48h] BYREF
  29   QArrayData *v30; // [xsp+40h] [xbp-40h] BYREF
     // ... excerpt omitted ...
  36   }
  37   sub_15947C(a1: &v31);
  38   QString::toUtf8_helper(this: a1, a2: v4);
  39   v29 = (QArrayData *)&QArrayData::shared_null;
     // ... excerpt omitted ...
  49   }
  50   if ( CCCryptorCreateWithMode(
  51          op: 0,
  52          mode: 3u,
  53          alg: 6u,
  54          padding: 0,
  55          iv: "2005120420CPackedProblemReport",
  56          key: (char *)v5 + v6,
  57          keyLength: v5[1],
  58          tweak: nullptr,
  59          tweakLength: 0,
     // ... excerpt omitted ...
  89   }
  90   if ( CCCryptorUpdate(
  91          cryptorRef: v7,
  92          dataIn: (char *)v8 + v9,
     // ... excerpt omitted ...
 108   }
 109   if ( CCCryptorFinal(
 110          cryptorRef: v14,
 111          dataOut: (char *)v13 + v15 + dataOutMoved,
     // ... excerpt omitted ...
 115 LABEL_19:
 116     CCCryptorRelease(cryptorRef);
 117     sub_1F43AC(a1: "", a2: "prl_bf_wrapper", a3: 0, a4: "Failed to encrypt data");
 118     *a2 = &QArrayData::shared_null;
     // ... excerpt omitted ...
 121   QByteArray::resize(this: (QByteArray *)&v29, a2: v26 + dataOutMoved);
 122   CCCryptorRelease(cryptorRef);
 123   QByteArray::toBase64(this: (QByteArray *)&v29);
 124   v21 = nullptr;
```

## G8 Social sign in variants

`0xf46d4`

```cpp
     // ... excerpt omitted ...
  67   {
  68     case 1:
  69       if ( off_37B940[0] != nullptr )
  70         v5 = strlen(__s: off_37B940[0]);
     // ... excerpt omitted ...
  93       v41 = (QtSharedPointer::ExternalRefCountData *)operator new(__sz: 0x70u);
  94       CTaskFacebookLogin::CTaskFacebookLogin(a1: v41, a2: &v54, a3: *((unsigned int *)this + 14));
  95       v43 = QtSharedPointer::ExternalRefCountData::getAndRef(this: v41, a2: v42);
  96       v44 = *((void **)this + 13);
     // ... excerpt omitted ...
 112       goto LABEL_94;
 113     case 2:
 114       if ( off_37B948[0] != nullptr )
 115         v6 = strlen(__s: off_37B948[0]);
     // ... excerpt omitted ...
 152       v32 = (QtSharedPointer::ExternalRefCountData *)operator new(__sz: 0x68u);
 153       CTaskGoogleLogin::CTaskGoogleLogin(a1: v32, a2: &v57);
 154       v54 = (QArrayData *)CTaskGoogleLogin::webAuthFinished;
 155       v55 = nullptr;
     // ... excerpt omitted ...
 201       goto LABEL_103;
 202     case 3:
 203       v7 = (_DWORD *)QString::fromAscii_helper(
 204                        this: (QString *)"com.parallels.desktop.console",
     // ... excerpt omitted ...
 280       }
 281       CTaskAppleLogin::CTaskAppleLogin(a1: v15, a2: &v54, a3: v18, a4: *((unsigned int *)this + 14));
 282       v59.d = CTaskAppleLogin::webAuthFinished;
 283       v60 = 0;
```