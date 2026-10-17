# Parallels edition check evidence

Original code from static IDA analysis of Parallels Desktop 27.0.3 build 58680 ARM64. No instructions were patched. Service and client addresses use image base 0x100000000; SDK addresses use slice image base zero. Decompiled signatures may misidentify hidden X8 return objects. Assembly locations below identify the original instructions. Selected pseudocode is accompanied by original line numbers.

## E1 Service license status

Binary `service`, function `0x100279b3c`.

```cpp
     // ... omitted ...
   1 __int64 __fastcall sub_100279B3C(__int64 a1)
   2 {
   3   if ( (*(_BYTE *)(a1 + 56) & 1) != 0 )
   4     return 4294910286LL;
   5   else
   6     return sub_10031A878(a1: a1 + 24);
   7 }
```

```asm
0x100279b3c LDRB            W8, [X0,#0x38]
0x100279b40 TBZ             W8, #0, loc_100279B4C
0x100279b44 MOV             W0, #0xFFFF214E
0x100279b48 RET
0x100279b4c ADD             X0, X0, #0x18
0x100279b50 B               sub_10031A878
```

## E2 VM startup license and edition

Binary `service`, function `0x100057ca4`.

```cpp
     // ... omitted ...
 287             if ( (unsigned int)sub_1002E9510(a1: v91) != 0 )
 288             {
 289               sub_100025788(a1: &v93, a2: qword_1007225C8);
 290               v35 = sub_100013368(a1: *((_QWORD *)v93 + 1) + 72LL);
 291               v36 = v94;
 292               if ( v94 != nullptr && atomic_fetch_add((atomic_ullong *volatile)v94 + 1, 0xFFFFFFFFFFFFFFFFLL) == 0 )
 293               {
 294                 v37 = v35;
 295                 (*(void (__fastcall **)(QArrayData *))(*(_QWORD *)v36 + 16LL))(a1: v36);
 296                 std::__shared_weak_count::__release_weak(this: (std::__shared_weak_count *)v36);
 297                 v35 = v37;
 298               }
 299               if ( (v35 & 0xFFFFFFFE) != 2 )
 300               {
 301                 v50 = *a1;
 302                 v51 = *((atomic_uint **)*a1 + 4);
 303                 v90 = v51;
 304                 if ( (unsigned int)(*v51 - 1) <= 0xFFFFFFFD )
 305                 {
     // ... omitted ...
 315                   a2: "disp",
 316                   a3: 15,
 317                   a4: 0,
 318                   a5: "Start VM: %s, uuid=%s cannot be done as x86 Emulation is supported only on Professional and Business license",
 319                   (const char *)&v90,
 320                   (const char *)&v89);
 321                 sub_100009FBC(a1: &v89);
 322                 sub_100009FBC(a1: &v90);
 323 LABEL_149:
 324                 v8 = (__int64)v92;
     // ... omitted ...
 579       goto LABEL_163;
 580     }
 581     sub_100025788(a1: &v93, a2: qword_1007225C8);
 582     if ( (unsigned int)sub_100279B3C(a1: *((_QWORD *)v93 + 1) + 48LL) == 0 )
 583     {
 584       v42 = v94;
 585       if ( v94 != nullptr && atomic_fetch_add((atomic_ullong *volatile)v94 + 1, 0xFFFFFFFFFFFFFFFFLL) == 0 )
 586       {
 587         (*(void (__fastcall **)(QArrayData *))(*(_QWORD *)v42 + 16LL))(a1: v42);
 588         std::__shared_weak_count::__release_weak(this: (std::__shared_weak_count *)v42);
 589       }
 590       goto LABEL_32;
 591     }
 592     v23 = sub_100279B3C(a1: *((_QWORD *)v93 + 1) + 48LL);
 593     v24 = v23;
 594     v25 = *((atomic_uint **)*a1 + 1);
 595     v98 = v25;
 596     if ( (unsigned int)(*v25 - 1) <= 0xFFFFFFFD )
 597       atomic_fetch_add(v25, 1u);
 598     v26 = (const char *)sub_10056E3B4(a1: v23);
```

```asm
0x100057fb8 LDR             X8, [SP,#0x250+var_190]
0x100057fbc LDR             X8, [X8,#8]
0x100057fc0 ADD             X0, X8, #0x30 ; '0'
0x100057fc4 BL              sub_100279B3C
0x100057fc8 CBZ             W0, loc_100058320
0x100057fcc LDR             X8, [SP,#0x250+var_190]
0x100057fd0 LDR             X8, [X8,#8]
0x100057fd4 ADD             X0, X8, #0x30 ; '0'
0x100057fd8 BL              sub_100279B3C
0x100057fdc MOV             X22, X0
0x100058244 LDR             X0, [SP,#0x250+var_1A0]
0x100058248 BL              sub_1002E9510
0x10005824c CBZ             W0, loc_1000582B0
0x100058250 LDR             X0, [X26]
0x100058254 ADD             X8, SP, #0x250+var_190
0x100058258 BL              sub_100025788
0x10005825c LDR             X8, [SP,#0x250+var_190]
0x100058260 LDR             X8, [X8,#8]
0x100058264 ADD             X0, X8, #0x48 ; 'H'
0x100058268 BL              sub_100013368
0x10005826c LDR             X23, [SP,#0x250+var_188]
0x100058270 CBZ             X23, loc_1000582A4
0x100058274 ADD             X8, X23, #8
0x100058278 MOV             X9, #0xFFFFFFFFFFFFFFFF
0x10005827c LDADDAL         X9, X8, [X8]
0x100058280 CBNZ            X8, loc_1000582A4
0x100058284 LDR             X8, [X23]
0x100058288 LDR             X8, [X8,#0x10]
0x10005828c MOV             X28, X0
0x100058290 MOV             X0, X23
0x100058294 BLR             X8
0x100058298 MOV             X0, X23; this
0x10005829c BL              std::__shared_weak_count::__release_weak(void)
0x1000582a0 MOV             X0, X28
0x1000582a4 AND             W8, W0, #0xFFFFFFFE
0x1000582a8 CMP             W8, #2
0x1000582ac B.NE            loc_1000584AC
0x1000582b0 ADD             W8, W24, #8
```

## E3 Snapshot switch validity

Binary `service`, function `0x10005ebfc`.

```cpp
     // ... omitted ...
  66   if ( *(_DWORD *)(*a1 + 244) == 0 )
  67   {
  68     sub_100025788(a1: &v48, a2: qword_1007225C8);
  69     if ( (unsigned int)sub_100279B3C(a1: *((_QWORD *)v48 + 1) + 48LL) != 0 )
  70     {
  71       v14 = sub_100279B3C(a1: *((_QWORD *)v48 + 1) + 48LL);
  72       v15 = v14;
  73       v16 = *(QArrayData **)(*a1 + 8);
  74       v47 = v16;
  75       if ( (unsigned int)(*(_DWORD *)v16 - 1) <= 0xFFFFFFFD )
  76         atomic_fetch_add((atomic_uint *volatile)v16, 1u);
  77       v17 = (const char *)sub_10056E3B4(a1: v14);
     // ... omitted ...
  80         a2: "disp",
  81         a3: 3,
  82         a4: 0,
  83         a5: "Failed to switch VM %s to snapshot: license status %#x (%s)",
  84         (const char *)&v47,
  85         v15,
  86         v17);
  87       v19 = v47;
  88       if ( *(_DWORD *)v47 != -1 )
  89       {
```

```asm
0x10005ed00 ADD             X8, SP, #0xE0+var_90
0x10005ed04 BL              sub_100025788
0x10005ed08 LDR             X8, [SP,#0xE0+var_90]
0x10005ed0c LDR             X8, [X8,#8]
0x10005ed10 ADD             X0, X8, #0x30 ; '0'
0x10005ed14 BL              sub_100279B3C
0x10005ed18 CBZ             W0, loc_10005EE9C
0x10005ed1c LDR             X8, [SP,#0xE0+var_90]
0x10005ed20 LDR             X8, [X8,#8]
0x10005ed24 ADD             X0, X8, #0x30 ; '0'
0x10005ed28 BL              sub_100279B3C
0x10005ed2c MOV             X21, X0
```

## E4 Feature matrix producer

Binary `service`, function `0x1001415d8`.

```cpp
     // ... omitted ...
   1 __int64 __fastcall sub_1001415D8(__int64 a1)
   2 {
   3   __int64 v2; // x0
   4   int isDefaultPlainDiskAllowed; // w0
   5   std::__shared_weak_count *v4; // x20
   6   __int64 v5; // x1
   7   int v6; // w2
   8   int v7; // w0
   9   std::__shared_weak_count *v8; // x20
  10   int v9; // w21
  11   __int64 v10; // x0
  12   unsigned __int64 v11; // x20
  13   atomic_uint *v12; // x20
  14   __int64 v13; // x21
  15   atomic_uint v14; // w8
  16   atomic_uint *v15; // x0
  17   atomic_uint v16; // w8
  18   __int64 result; // x0
  19   atomic_uint v18; // w8
  20   int v19; // w22
  21   atomic_uint *v20; // [xsp+8h] [xbp-48h] BYREF
  22   unsigned __int64 v21; // [xsp+10h] [xbp-40h] BYREF
  23   std::__shared_weak_count *v22; // [xsp+18h] [xbp-38h]
  24   atomic_uint *v23; // [xsp+20h] [xbp-30h] BYREF
  25   char v24; // [xsp+2Fh] [xbp-21h] BYREF
  26
  27   v23 = (atomic_uint *)&QHashData::shared_null;
  28   LODWORD(v21) = 12;
  29   sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
  30   LODWORD(v21) = 2;
  31   sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
  32   LODWORD(v21) = 14;
  33   sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
  34   LODWORD(v21) = 13;
  35   sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
  36   v2 = sub_1000248C4(a1: qword_1007225C8);
  37   sub_10001F6D0(a1: &v21, a2: v2);
  38   isDefaultPlainDiskAllowed = CDispWorkspacePreferences::isDefaultPlainDiskAllowed(this: *(CDispWorkspacePreferences **)(v21 + 8));
  39   v4 = v22;
  40   if ( v22 == nullptr || atomic_fetch_add(&v22->__shared_owners_, 0xFFFFFFFFFFFFFFFFLL) != 0 )
  41   {
  42     if ( isDefaultPlainDiskAllowed == 0 )
  43       goto LABEL_5;
  44     goto LABEL_4;
  45   }
  46   v19 = isDefaultPlainDiskAllowed;
  47   ((void (__fastcall *)(std::__shared_weak_count *))v4->__on_zero_shared)(a1: v4);
  48   std::__shared_weak_count::__release_weak(this: v4);
  49   if ( v19 != 0 )
  50   {
  51 LABEL_4:
  52     LODWORD(v21) = 5;
  53     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
  54   }
  55 LABEL_5:
  56   if ( (sub_100512404() & 1) == 0 )
  57   {
  58     LODWORD(v21) = 16;
  59     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
  60     LODWORD(v21) = 27;
  61     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
  62   }
  63   sub_100025788(a1: &v21, a2: qword_1007225C8);
  64   v7 = sub_100013368(a1: *(_QWORD *)(v21 + 8) + 72LL, a2: v5, a3: v6);
  65   v8 = v22;
  66   if ( v22 != nullptr && atomic_fetch_add(&v22->__shared_owners_, 0xFFFFFFFFFFFFFFFFLL) == 0 )
  67   {
  68     v9 = v7;
  69     ((void (__fastcall *)(std::__shared_weak_count *))v8->__on_zero_shared)(a1: v8);
  70     std::__shared_weak_count::__release_weak(this: v8);
  71     v7 = v9;
  72   }
  73   if ( (v7 & 0xFFFFFFFE) == 2 )
  74   {
  75     LODWORD(v21) = 17;
  76     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
  77     LODWORD(v21) = 19;
  78     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
  79     LODWORD(v21) = 21;
  80     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
  81     LODWORD(v21) = 22;
  82     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
  83     LODWORD(v21) = 23;
  84     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
  85     LODWORD(v21) = 24;
  86     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
  87     LODWORD(v21) = 25;
  88     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
  89     LODWORD(v21) = 26;
  90     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
  91     LODWORD(v21) = 28;
  92     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
  93     LODWORD(v21) = 29;
  94     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
  95     LODWORD(v21) = 30;
  96     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
  97     LODWORD(v21) = 31;
  98     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
  99     LODWORD(v21) = 32;
 100     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
 101     LODWORD(v21) = 33;
 102     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
 103     LODWORD(v21) = 34;
 104     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
 105     LODWORD(v21) = 37;
 106     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
 107     LODWORD(v21) = 38;
 108     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
 109     LODWORD(v21) = 39;
 110     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
 111     LODWORD(v21) = 40;
 112     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
 113     LODWORD(v21) = 41;
 114     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
 115     LODWORD(v21) = 43;
 116     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
 117     LODWORD(v21) = 45;
 118     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
 119     LODWORD(v21) = 46;
 120     sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
 121     if ( (unsigned int)sub_1005765F0(a1: 1, a2: 15, a3: 6, a4: 0) != 0 )
 122     {
 123       v10 = sub_100542D58();
 124       if ( v10 == 0x10000000000LL || v10 == 0x1000000000LL )
 125       {
 126         LODWORD(v21) = 20;
 127         sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
 128       }
 129     }
 130   }
 131   LODWORD(v21) = 44;
 132   sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
 133   LODWORD(v21) = 42;
 134   sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
 135   LODWORD(v21) = 18;
 136   sub_100141DC4(a1: &v23, a2: &v21, a3: &v24);
 137   v11 = a1 + 16;
 138   v21 = a1 + 16;
 139   if ( (((_DWORD)a1 + 16) & 1) == 0 )
 140   {
 141     QReadWriteLock::lockForWrite(this: (QReadWriteLock *)(a1 + 16));
 142     v11 |= 1u;
 143     v21 = v11;
 144   }
 145   sub_100386ACC(a1: a1 + 24, a2: &v23);
 146   if ( (v11 & 1) != 0 )
 147   {
 148     v21 = v11 & 0xFFFFFFFFFFFFFFFELL;
 149     QReadWriteLock::unlock(this: (QReadWriteLock *)(v11 & 0xFFFFFFFFFFFFFFFELL));
 150   }
 151   v12 = v23;
 152   v20 = v23;
 153   if ( (unsigned int)(v23[4] - 1) <= 0xFFFFFFFD )
 154   {
 155     atomic_fetch_add(v23 + 4, 1u);
 156     v12 = v20;
 157   }
 158   if ( (v12[10] & 1) == 0 && (unsigned int)v12[4] >= 2 )
 159   {
 160     v13 = QHashData::detach_helper(a1: v12, a2: sub_100033EC0, a3: nullsub_17, a4: 16, a5: 8);
 161     v14 = v12[4];
 162     if ( v14 != -1 )
 163     {
 164       if ( v14 == 0 )
 165       {
 166 LABEL_27:
 167         QHashData::free_helper(a1: v12, a2: nullsub_17);
 168         goto LABEL_28;
 169       }
 170       if ( atomic_fetch_add(v12 + 4, 0xFFFFFFFF) == 1 )
 171       {
 172         v12 = v20;
 173         goto LABEL_27;
 174       }
 175     }
 176 LABEL_28:
 177     v20 = (atomic_uint *)v13;
 178   }
 179   sub_1002FDD70(a1, a2: &v20);
 180   v15 = v20;
 181   v16 = v20[4];
 182   if ( v16 != -1 )
 183   {
 184     if ( v16 != 0 )
 185     {
 186       if ( atomic_fetch_add(v20 + 4, 0xFFFFFFFF) != 1 )
 187         goto LABEL_34;
 188       v15 = v20;
 189     }
 190     QHashData::free_helper(a1: v15, a2: nullsub_17);
 191   }
 192 LABEL_34:
 193   if ( (v21 & 1) != 0 )
 194   {
 195     v21 &= ~1uLL;
 196     QReadWriteLock::unlock(this: (QReadWriteLock *)v21);
 197   }
 198   result = (__int64)v23;
 199   v18 = v23[4];
 200   if ( v18 != -1 )
 201   {
 202     if ( v18 != 0 )
 203     {
 204       if ( atomic_fetch_add(v23 + 4, 0xFFFFFFFF) != 1 )
 205         return result;
 206       result = (__int64)v23;
 207     }
 208     return QHashData::free_helper(a1: result, a2: nullsub_17);
 209   }
 210   return result;
 211 }
```

```asm
0x1001416f8 LDR             X8, [SP,#0x50+var_40]
0x1001416fc LDR             X8, [X8,#8]
0x100141700 ADD             X0, X8, #0x48 ; 'H'
0x100141704 BL              sub_100013368
0x100141708 LDR             X20, [SP,#0x50+var_38]
0x10014170c CBZ             X20, loc_100141740
0x100141710 ADD             X8, X20, #8
0x100141714 MOV             X9, #0xFFFFFFFFFFFFFFFF
0x100141718 LDADDAL         X9, X8, [X8]
0x10014171c CBNZ            X8, loc_100141740
0x100141720 LDR             X8, [X20]
0x100141724 LDR             X8, [X8,#0x10]
0x100141728 MOV             X21, X0
0x10014172c MOV             X0, X20
0x100141730 BLR             X8
0x100141734 MOV             X0, X20; this
0x100141738 BL              std::__shared_weak_count::__release_weak(void)
0x10014173c MOV             X0, X21
0x100141740 AND             W8, W0, #0xFFFFFFFE
0x100141744 CMP             W8, #2
0x100141748 B.NE            loc_1001419C0
0x10014174c MOV             W8, #0x11
0x100141750 STR             W8, [SP,#0x50+var_40]
0x100141754 ADD             X0, SP, #0x50+var_30
0x100141758 ADD             X1, SP, #0x50+var_40
0x10014175c SUB             X2, X29, #-var_21
```

## E5 Edition reader

Binary `service`, function `0x100013368`.

```cpp
     // ... omitted ...
   1 __int64 __fastcall sub_100013368(__int64 a1, __int64 a2, int a3)
   2 {
   3   unsigned __int64 v4; // x3
   4   unsigned int v5; // w19
   5   QArrayData *v6; // x0
   6   int v8; // [xsp+4h] [xbp-1Ch] BYREF
   7   QArrayData *v9; // [xsp+8h] [xbp-18h] BYREF
   8
   9   v9 = (QArrayData *)QString::fromAscii_helper(this: (QString *)"edition", a2: (const char *)7, a3);
  10   v8 = 1;
  11   v5 = sub_10001340C(a1, a2: &v9, a3: &v8);
  12   v6 = v9;
  13   if ( *(_DWORD *)v9 != -1 )
  14   {
  15     if ( *(_DWORD *)v9 != 0 )
  16     {
  17       if ( atomic_fetch_add((atomic_uint *volatile)v9, 0xFFFFFFFF) != 1 )
  18         goto LABEL_6;
  19       v6 = v9;
  20     }
  21     QArrayData::deallocate(this: v6, a2: (QArrayData *)2, a3: 8u, a4: v4);
  22   }
  23 LABEL_6:
  24   if ( v5 >= 4 )
  25     return 1;
  26   else
  27     return v5;
  28 }
```

## E6 Resource validation producer

Binary `service`, function `0x1000a238c`.

```cpp
     // ... omitted ...
  86     return;
  87   v2 = sub_100025788(a1: &v80, a2: qword_1007225C8);
  88   if ( (sub_100025398(a1: v2) & 1) != 0
  89     || (unsigned int)sub_100013368(a1: *(_QWORD *)(v80 + 8) + 72LL, a2: v3, a3: v4) == 1 )
  90   {
  91     v5 = *(_QWORD *)(v80 + 8);
  92     v82 = (QArrayData *)QString::fromAscii_helper(this: (QString *)"cpu_limit", a2: (const char *)9, a3: v4);
  93     LODWORD(v79) = 8;
  94     v7 = sub_10001340C(a1: v5 + 72, a2: &v82, a3: &v79);
  95     v8 = v82;
  96     if ( *(_DWORD *)v82 != -1 )
  97     {
  98       if ( *(_DWORD *)v82 != 0 )
     // ... omitted ...
 106 LABEL_9:
 107     VmHardwareList = (CVmHardware *)CVmConfiguration::getVmHardwareList(this: *(CVmConfiguration **)(a1 + 16));
 108     Cpu = (CVmCpu *)CVmHardware::getCpu(this: VmHardwareList);
 109     if ( (unsigned int)CVmCpu::getNumber(this: Cpu) <= v7 )
 110       goto LABEL_48;
 111     LODWORD(v82) = -26501;
 112     sub_100070250(a1: a1 + 48, a2: &v82);
 113     v82 = (QArrayData *)&QListData::shared_null;
 114     v78.var0 = (void *)QString::fromAscii_helper(this: (QString *)"%1", a2: (const char *)2, a3: v12);
 115     QString::arg(a1: &v79, a2: &v78, a3: v7, a4: 0, a5: 10, a6: 32);
 116     sub_100016FAC(a1: &v82, a2: &v79);
 117     v14 = v79;
     // ... omitted ...
 206     {
 207 LABEL_48:
 208       v31 = *(_QWORD *)(v80 + 8);
 209       v82 = (QArrayData *)QString::fromAscii_helper(this: (QString *)"ram_limit", a2: (const char *)9, a3: v11);
 210       LODWORD(v79) = 0x2000;
 211       v33 = sub_10001340C(a1: v31 + 72, a2: &v82, a3: &v79);
 212       v34 = v82;
 213       if ( *(_DWORD *)v82 != -1 )
 214       {
 215         if ( *(_DWORD *)v82 != 0 )
     // ... omitted ...
 223 LABEL_53:
 224       v35 = (CVmHardware *)CVmConfiguration::getVmHardwareList(this: *(CVmConfiguration **)(a1 + 16));
 225       Memory = (CVmMemory *)CVmHardware::getMemory(this: v35);
 226       if ( (unsigned int)CVmMemory::getRamSize(this: Memory) <= v33 )
 227         goto LABEL_108;
 228       v37 = v33 >> 10;
 229       v82 = (QArrayData *)&QListData::shared_null;
 230       v39 = a1 + 48;
 231       v38 = *(_DWORD **)(a1 + 48);
 232       LODWORD(v40) = v38[3];
 233       if ( (_DWORD)v40 != v38[2] )
     // ... omitted ...
 239           LODWORD(v40) = *(_DWORD *)(*(_QWORD *)v39 + 12LL);
 240         }
 241         v41 = *(_DWORD **)&v38[2 * (int)v40 + 2];
 242         if ( *v41 == -26501 )
 243         {
 244           if ( *v38 >= 2u )
 245           {
 246             sub_100070C28(a1: a1 + 48, a2: (unsigned int)v38[1]);
 247             v38 = *(_DWORD **)v39;
 248             v40 = *(int *)(*(_QWORD *)v39 + 12LL);
 249             v41 = *(_DWORD **)(*(_QWORD *)v39 + 8 * v40 + 8);
 250           }
 251           *v41 = -26505;
 252           v77 = v40 - v38[2];
 253           v42 = sub_1000B8CD8(a1: a1 + 56, a2: &v77);
 254           v78.var0 = (void *)QString::fromAscii_helper(this: (QString *)"%1", a2: (const char *)2, a3: v43);
 255           QString::arg(a1: &v79, a2: &v78, a3: v37, a4: 0, a5: 10, a6: 32);
 256           sub_100016FAC(a1: v42, a2: &v79);
 257           v45 = v79;
     // ... omitted ...
 280           goto LABEL_65;
 281         }
 282       }
 283       LODWORD(v79) = -26502;
 284       sub_100070250(a1: a1 + 48, a2: &v79);
 285       v78.var0 = (void *)QString::fromAscii_helper(this: (QString *)"%1", a2: (const char *)2, a3: v47);
 286       QString::arg(a1: &v79, a2: &v78, a3: v37, a4: 0, a5: 10, a6: 32);
 287       sub_100016FAC(a1: &v82, a2: &v79);
 288       v49 = v79;
 289       if ( *(_DWORD *)v79 != -1 )
     // ... omitted ...
 378         QHashData::free_helper();
 379       v63 = v82;
 380       if ( *(_DWORD *)v82 == -1 )
 381         goto LABEL_108;
 382       if ( *(_DWORD *)v82 != 0 )
 383       {
 384         if ( atomic_fetch_add((atomic_uint *volatile)v82, 0xFFFFFFFF) != 1 )
 385           goto LABEL_108;
 386         v63 = v82;
 387       }
 388       v64 = *((int *)v63 + 2);
 389       v65 = *((int *)v63 + 3);
 390       if ( (_DWORD)v65 == (_DWORD)v64 )
 391       {
 392 LABEL_107:
 393         QListData::dispose(a1: v63);
 394         goto LABEL_108;
 395       }
 396       v72 = 8 * v65;
 397       v73 = (atomic_uint **)((char *)v63 + v72 + 8);
 398       v74 = 8 * v64 - v72;
 399       while ( 1 )
 400       {
     // ... omitted ...
 455         goto LABEL_47;
 456     }
 457   }
 458 LABEL_108:
 459   v66 = v81;
 460   if ( v81 != nullptr && atomic_fetch_add(&v81->__shared_owners_, 0xFFFFFFFFFFFFFFFFLL) == 0 )
 461   {
 462     ((void (__fastcall *)(std::__shared_weak_count *))v66->__on_zero_shared)(a1: v66);
 463     std::__shared_weak_count::__release_weak(this: v66);
 464   }
```

```asm
0x1000a23c0 BL              sub_100025788
0x1000a23c4 BL              sub_100025398
0x1000a23c8 TBNZ            W0, #0, loc_1000A23E4
0x1000a23cc LDR             X8, [SP,#0x70+var_50]
0x1000a23d0 LDR             X8, [X8,#8]
0x1000a23d4 ADD             X0, X8, #0x48 ; 'H'
0x1000a23d8 BL              sub_100013368
0x1000a23dc CMP             W0, #1
0x1000a23e0 B.NE            loc_1000A2AE0
0x1000a23e4 LDR             X8, [SP,#0x70+var_50]
0x1000a23e8 LDR             X20, [X8,#8]
0x1000a23ec ADRL            X0, aCpuLimit; "cpu_limit"
0x1000a23f0 ADRL            X0, aCpuLimit; "cpu_limit"
0x1000a23f4 MOV             W1, #9; char *
0x1000a23f8 BL              QString::fromAscii_helper(char const*,int)
0x1000a23fc STR             X0, [SP,#0x70+var_40]
0x1000a2400 MOV             W8, #8
0x1000a2404 STR             W8, [SP,#0x70+var_58]
0x1000a2408 ADD             X0, X20, #0x48 ; 'H'
0x1000a240c ADD             X1, SP, #0x70+var_40
0x1000a2410 ADD             X2, SP, #0x70+var_58
0x1000a2450 LDR             X0, [X19,#0x10]; this
0x1000a2454 BL              CVmConfiguration::getVmHardwareList(void)
0x1000a2458 BL              CVmHardware::getCpu(void)
0x1000a245c BL              CVmCpu::getNumber(void)
0x1000a2460 CMP             W0, W20
0x1000a2464 B.LS            loc_1000A26C0
0x1000a2468 MOV             W8, #0xFFFF987B
0x1000a246c STR             W8, [SP,#0x70+var_40]
0x1000a2470 ADD             X0, X19, #0x30 ; '0'
0x1000a2474 ADD             X1, SP, #0x70+var_40
0x1000a2478 BL              sub_100070250
0x1000a272c LDR             X0, [X19,#0x10]; this
0x1000a2730 BL              CVmConfiguration::getVmHardwareList(void)
0x1000a2734 BL              CVmHardware::getMemory(void)
0x1000a2738 BL              CVmMemory::getRamSize(void)
0x1000a273c CMP             W0, W20
0x1000a2740 B.LS            loc_1000A2AE0
0x1000a2744 LSR             W20, W20, #0xA
0x1000a2748 ADRP            X8, #__ZN9QListData11shared_nullE_ptr@PAGE
```

## E7 Direct CPU change restriction

Binary `service`, function `0x100238afc`.

```cpp
     // ... omitted ...
   1 __int64 __fastcall sub_100238AFC(__int64 a1, CVmConfiguration **a2, CVmConfiguration **a3)
   2 {
   3   CVmHardware *VmHardwareList; // x0
   4   CVmCpu *Cpu; // x0
   5   CVmHardware *v7; // x0
   6   CVmCpu *v8; // x0
   7   int v9; // w2
   8   int Number; // w19
   9   __int64 v11; // x20
  10   unsigned __int64 v12; // x3
  11   int v13; // w20
  12   QArrayData *v14; // x0
  13   const char *v15; // x0
  14   __int64 v16; // x19
  15   std::__shared_weak_count *v17; // x20
  16   __int64 v19; // [xsp+10h] [xbp-30h] BYREF
  17   std::__shared_weak_count *v20; // [xsp+18h] [xbp-28h]
  18   int v21; // [xsp+24h] [xbp-1Ch] BYREF
  19   atomic_uint *v22; // [xsp+28h] [xbp-18h] BYREF
  20
  21   sub_100025788(a1: &v19, a2: qword_1007225C8);
  22   VmHardwareList = (CVmHardware *)CVmConfiguration::getVmHardwareList(this: *a2);
  23   Cpu = (CVmCpu *)CVmHardware::getCpu(this: VmHardwareList);
  24   LODWORD(a2) = CVmCpu::getNumber(this: Cpu);
  25   v7 = (CVmHardware *)CVmConfiguration::getVmHardwareList(this: *a3);
  26   v8 = (CVmCpu *)CVmHardware::getCpu(this: v7);
  27   Number = CVmCpu::getNumber(this: v8);
  28   if ( (_DWORD)a2 == Number )
  29   {
  30 LABEL_10:
  31     v16 = 0;
  32     v17 = v20;
  33     if ( v20 == nullptr )
  34       return v16;
  35     goto LABEL_11;
  36   }
  37   v11 = *(_QWORD *)(v19 + 8);
  38   v22 = (atomic_uint *)QString::fromAscii_helper(this: (QString *)"cpu_limit", a2: (const char *)9, a3: v9);
  39   v21 = 8;
  40   v13 = sub_10001340C(a1: v11 + 72, a2: &v22, a3: &v21);
  41   v14 = (QArrayData *)v22;
  42   if ( *v22 != -1 )
  43   {
  44     if ( *v22 != 0 )
  45     {
  46       if ( atomic_fetch_add(v22, 0xFFFFFFFF) != 1 )
  47         goto LABEL_7;
  48       v14 = (QArrayData *)v22;
  49     }
  50     QArrayData::deallocate(this: v14, a2: (QArrayData *)2, a3: 8u, a4: v12);
  51   }
  52 LABEL_7:
  53   if ( Number <= v13 )
  54     goto LABEL_10;
  55   v15 = (const char *)sub_10056E3B4(a1: 4294940795LL);
  56   v16 = 4294940795LL;
  57   sub_1005756CC(a1: "", a2: "disp", a3: 0, a4: "Restrictions check failed with error %#x %s", -26501, v15);
  58   v17 = v20;
  59   if ( v20 == nullptr )
  60     return v16;
  61 LABEL_11:
  62   if ( atomic_fetch_add(&v17->__shared_owners_, 0xFFFFFFFFFFFFFFFFLL) == 0 )
  63   {
  64     ((void (__fastcall *)(std::__shared_weak_count *))v17->__on_zero_shared)(a1: v17);
  65     std::__shared_weak_count::__release_weak(this: v17);
  66   }
  67   return v16;
  68 }
```

```asm
0x100238bc4 CMP             W19, W20
0x100238bc8 B.LE            loc_100238C08
0x100238bcc MOV             W0, #0xFFFF987B
0x100238bd0 BL              sub_10056E3B4
0x100238bd4 MOV             W19, #0xFFFF987B
0x100238bd8 STP             X19, X0, [SP,#0x40+var_40]
0x100238bdc ADRL            X0, asc_1006255A0; ""
0x100238be0 ADRL            X0, asc_1006255A0; ""
```

## E8 Automatic CPU sizing

Binary `service`, function `0x1002e8fec`.

```cpp
     // ... omitted ...
  21   if ( (_DWORD)result != 0 )
  22   {
  23     v10 = CVmProfileHelper::calc_auto_cpu(this: a1, a2: this, a3: v9);
  24     v19 = (QArrayData *)QString::fromAscii_helper(this: (QString *)"cpu_limit", a2: (const char *)9, a3: v11);
  25     v18 = 8;
  26     v14 = sub_10001340C(a1: a2, a2: &v19, a3: &v18);
  27     v15 = v19;
  28     if ( *(_DWORD *)v19 != -1 )
  29     {
  30       if ( *(_DWORD *)v19 == 0 )
     // ... omitted ...
  40       }
  41     }
  42 LABEL_7:
  43     if ( v10 > v14 )
  44     {
  45       v19 = (QArrayData *)QString::fromAscii_helper(this: (QString *)"cpu_limit", a2: (const char *)9, a3: v12);
  46       v18 = 8;
  47       v10 = sub_10001340C(a1: a2, a2: &v19, a3: &v18);
  48       v17 = v19;
  49       if ( *(_DWORD *)v19 == -1 )
  50         goto LABEL_13;
  51       if ( *(_DWORD *)v19 != 0 )
     // ... omitted ...
  63     }
  64     else
  65     {
  66       CVmCpu::setNumber(this: Cpu, a2: v10);
  67       sub_100147EEC(a1: this);
  68       return 1;
  69     }
  70   }
  71   return result;
  72 }
```

```asm
0x1002e909c CMP             W21, W23
0x1002e90a0 B.LS            loc_1002E9108
0x1002e90a4 ADRL            X0, aCpuLimit; "cpu_limit"
0x1002e90a8 ADRL            X0, aCpuLimit; "cpu_limit"
0x1002e90ac MOV             W1, #9; char *
0x1002e90b0 BL              QString::fromAscii_helper(char const*,int)
```

## E9 Automatic RAM sizing

Binary `service`, function `0x1002e9168`.

```cpp
     // ... omitted ...
   3   CVmHardware *VmHardwareList; // x0
   4   CVmMemory *Memory; // x20
   5   CHwMemorySettings *MemorySettings; // x0
   6   unsigned int MaxVmMemory; // w23
   7   const CVmConfiguration *v10; // x2
   8   unsigned int v11; // w0
   9   int v12; // w2
  10   unsigned int v13; // w22
  11   int v14; // w2
  12   unsigned __int64 v15; // x3
     // ... omitted ...
  22   VmHardwareList = (CVmHardware *)CVmConfiguration::getVmHardwareList(this);
  23   Memory = (CVmMemory *)CVmHardware::getMemory(this: VmHardwareList);
  24   MemorySettings = (CHwMemorySettings *)CHostHardwareInfoBase::getMemorySettings(this: a1);
  25   MaxVmMemory = CHwMemorySettings::getMaxVmMemory(this: MemorySettings);
  26   if ( (unsigned int)CVmMemory::isRamAutoSizeEnabled(this: Memory) != 0 )
  27   {
  28     v11 = CVmProfileHelper::calc_auto_ram(this: a1, a2: this, a3: v10);
  29     if ( v11 >= MaxVmMemory )
  30       v13 = MaxVmMemory;
  31     else
  32       v13 = v11;
  33     v24 = (QArrayData *)QString::fromAscii_helper(this: (QString *)"ram_limit", a2: (const char *)9, a3: v12);
  34     v23 = 0x2000;
  35     v16 = sub_10001340C(a1: a2, a2: &v24, a3: &v23);
  36     v17 = v24;
  37     if ( *(_DWORD *)v24 != -1 )
  38     {
  39       if ( *(_DWORD *)v24 == 0 )
     // ... omitted ...
  49       }
  50     }
  51 LABEL_10:
  52     if ( v13 > v16 )
  53     {
  54       v24 = (QArrayData *)QString::fromAscii_helper(this: (QString *)"ram_limit", a2: (const char *)9, a3: v14);
  55       v23 = 0x2000;
  56       v13 = sub_10001340C(a1: a2, a2: &v24, a3: &v23);
  57       v19 = v24;
  58       if ( *(_DWORD *)v24 != -1 )
  59       {
  60         if ( *(_DWORD *)v24 != 0 )
     // ... omitted ...
  72       v20 = Memory;
  73       v21 = v13;
  74 LABEL_20:
  75       CVmMemory::setRamSize(this: v20, a2: v21);
  76       sub_100147EEC(a1: this);
  77       return 1;
  78     }
  79     return 0;
  80   }
  81   if ( (unsigned int)CVmMemory::getRamSize(this: Memory) > MaxVmMemory )
  82   {
  83     v20 = Memory;
  84     v21 = MaxVmMemory;
  85     goto LABEL_20;
  86   }
  87   return 0;
  88 }
```

```asm
0x1002e9230 CMP             W22, W23
0x1002e9234 B.LS            loc_1002E929C
0x1002e9238 ADRL            X0, aRamLimit; "ram_limit"
0x1002e923c ADRL            X0, aRamLimit; "ram_limit"
0x1002e9240 MOV             W1, #9; char *
0x1002e9244 BL              QString::fromAscii_helper(char const*,int)
```

## E10 Signature acceptance

Binary `service`, function `0x100279b54`.

```cpp
     // ... omitted ...
  16   QArrayData *v22; // [xsp+30h] [xbp-40h] BYREF
  17   char v23; // [xsp+3Fh] [xbp-31h] BYREF
  18
  19   if ( (sub_1004626AC(a1: a2, a2: a3) & 1) != 0 )
  20   {
  21     QJsonObject::QJsonObject(this: (QJsonObject *)v20);
  22     v21 = (QArrayData *)&QArrayData::shared_null;
  23     v22 = (QArrayData *)&QArrayData::shared_null;
  24     if ( (sub_1003190C8(a1: v20, a2, a3) & 1) == 0 )
  25     {
  26       sub_1005756CC(a1: "", a2: "disp", a3: 0, a4: "unable to parse license info");
  27       v15 = 4294910293LL;
  28       goto LABEL_27;
  29     }
  30     if ( (a4 & 2) == 0 )
     // ... omitted ...
 132     }
 133     goto LABEL_21;
 134   }
 135   sub_1005756CC(a1: "", a2: "disp", a3: 0, a4: "Signature check failed for license info");
 136   return 4294910294LL;
 137 }
```

```asm
0x100279b74 MOV             X21, X1
0x100279b78 MOV             X19, X0
0x100279b7c MOV             X0, X1
0x100279b80 MOV             X1, X2
0x100279b84 BL              sub_1004626AC
0x100279b88 TBZ             W0, #0, loc_100279C9C
0x100279b8c ADD             X24, SP, #0x70+var_58
0x100279b90 ADD             X0, SP, #0x70+var_58; this
0x100279b94 BL              QJsonObject::QJsonObject(void)
0x100279b98 ADRP            X8, #__ZN10QArrayData11shared_nullE_ptr@PAGE
0x100279b9c LDR             X8, [X8,#__ZN10QArrayData11shared_nullE_ptr@PAGEOFF]; @rpath/QtCore.framework/Versions/5/QtCore
```

## E11 Client feature wrapper

Binary `client`, function `0x1000beca4`.

```cpp
     // ... omitted ...
   1 bool __fastcall sub_1000BECA4(Data *a1, __int64 a2)
   2 {
   3   Data v4; // x21
   4   int v5; // w22
   5   _BOOL4 v6; // w0
   6   int v7; // w2
   7   unsigned __int64 v8; // x3
   8   QArrayData *d; // x0
   9   QVariant v11; // [xsp+10h] [xbp-60h] BYREF
  10   QString v12; // [xsp+20h] [xbp-50h] BYREF
  11   _BYTE v13[16]; // [xsp+28h] [xbp-48h] BYREF
  12   QVariant v14; // [xsp+38h] [xbp-38h] BYREF
  13   int v15; // [xsp+4Ch] [xbp-24h] BYREF
  14
  15   v15 = 0;
  16   v4 = a1[16];
  17   v14.d.data = v4;
  18   if ( v4.l != 0 )
  19     ((void (__fastcall *)(_QWORD))PrlHandle_AddRef)(a1: (Data)v4.l);
  20   v5 = ((__int64 (__fastcall *)(_QWORD, _QWORD, _QWORD))PrlSrv_IsFeatureSupported)(a1: (Data)v4.l, a2, a3: &v15);
  21   if ( v4.l != 0 )
  22     ((void (__fastcall *)(_QWORD))PrlHandle_Free)(a1: (Data)v4.l);
  23   if ( v5 < 0 )
  24   {
  25     sub_10072D89C(
  26       a1: "",
  27       a2: "prl_client_app",
  28       a3: 0,
  29       a4: "Failed to get status of PFSM_VM_CONFIG_MERGE_SUPPORT feature, %#x",
  30       v5);
  31     return false;
  32   }
  33   if ( v15 != 0 )
  34   {
  35     v6 = sub_1004206CC(a1: a1[22].l, a2: 65664);
  36     if ( (unsigned int)(a2 - 16) <= 0x12 && v6 )
  37     {
  38       QSettings::QSettings(this: (QSettings *)v13, a2: nullptr);
  39       v12.d = (void *)QString::fromAscii_helper(
  40                         this: (QString *)"Advanced/TraditionalLook",
  41                         a2: (const char *)0x18,
  42                         a3: v7);
  43       *((_DWORD *)&v11.d + 2) = 0x80000000;
  44       v11.d.data.l = 0;
  45       QSettings::value(this: (QSettings *)v13, a2: &v12, a3: &v11);
  46       v15 = QVariant::toBool(this: &v14) ^ 1;
  47       QVariant::~QVariant(this: &v14);
  48       QVariant::~QVariant(this: &v11);
  49       d = (QArrayData *)v12.d;
  50       if ( *(_DWORD *)v12.d != -1 )
  51       {
  52         if ( *(_DWORD *)v12.d == 0 )
  53         {
  54 LABEL_13:
  55           QArrayData::deallocate(this: d, a2: (QArrayData *)2, a3: 8u, a4: v8);
  56           goto LABEL_14;
  57         }
  58         if ( atomic_fetch_add((atomic_uint *volatile)v12.d, 0xFFFFFFFF) == 1 )
  59         {
  60           d = (QArrayData *)v12.d;
  61           goto LABEL_13;
  62         }
  63       }
  64 LABEL_14:
  65       QSettings::~QSettings(this: (QSettings *)v13);
  66     }
  67   }
  68   if ( (unsigned int)a2 <= 0x2D && ((1LL << a2) & 0x200151000000LL) != 0 && (unsigned int)sub_100426E18() != 0 )
  69     v15 = 1;
  70   return v15 != 0;
  71 }
```

## E12 Client edition flag helpers

Binary `client`, function `0x100420670`.

```cpp
     // ... omitted ...
   1 bool __fastcall sub_100420670(__int64 a1, int a2)
   2 {
   3   int v2; // w8
   4   _BOOL4 v4; // w9
   5
   6   v2 = *(_DWORD *)(a1 + 56);
   7   v4 = a2 != 0 || v2 == 0;
   8   return (a2 & ~v2) == 0 && v4;
   9 }
```

```asm
0x100420670 LDR             W8, [X0,#0x38]
0x100420674 CMP             W1, #0
0x100420678 CCMP            W8, #0, #4, EQ
0x10042067c CSET            W9, EQ
0x100420680 BICS            WZR, W1, W8
0x100420684 CSEL            W0, WZR, W9, NE
0x100420688 RET
```

## E13 Client any flag helper

Binary `client`, function `0x1004206cc`.

```cpp
     // ... omitted ...
   1 bool __fastcall sub_1004206CC(__int64 a1, int a2)
   2 {
   3   return (*(_DWORD *)(a1 + 56) & a2) != 0;
   4 }
```

```asm
0x1004206cc LDR             W8, [X0,#0x38]
0x1004206d0 TST             X8, X1
0x1004206d4 CSET            W0, NE
0x1004206d8 RET
```

## E14 New VM resource clamp

Binary `client`, function `0x1000e8548`.

```cpp
     // ... omitted ...
   1 DisplayUtils *__fastcall sub_1000E8548(__int64 a1, Data *a2, CVmConfiguration *this, int a4)
   2 {
   3   CVmSettings *VmSettings; // x0
   4   CVmRunTimeOptions *VmRuntimeOptions; // x23
   5   char v10; // w0
   6   __int64 v11; // x0
   7   CVmHardware *VmHardwareList; // x0
   8   CVmMemory *Memory; // x0
   9   CVmHardware *v14; // x0
  10   CVmMemory *v15; // x0
  11   CVmHardware *v16; // x0
  12   CVmCpu *Cpu; // x0
  13   CVmHardware *v18; // x0
  14   CVmCpu *v19; // x0
  15   CVmSettings *v20; // x0
  16   CVmCommonOptions *VmCommonOptions; // x0
  17   DisplayUtils *result; // x0
  18   CVmHardware *v23; // x0
  19   CVmVideo *Video; // x0
  20   CVmHardware *v25; // x0
  21   CVmVideo *v26; // x0
  22
  23   VmSettings = (CVmSettings *)CVmConfiguration::getVmSettings(this);
  24   VmRuntimeOptions = (CVmRunTimeOptions *)CVmSettings::getVmRuntimeOptions(this: VmSettings);
  25   v10 = sub_10008A6C8();
  26   CVmRunTimeOptions::setHostRetinaEnabled(this: VmRuntimeOptions, a2: v10);
  27   v11 = sub_1000AF17C(a1: a2);
  28   CVmProfileHelper::set_vm_profile(a1, a2: v11, a3: this);
  29   if ( !sub_1000BECA4(a1: a2, a2: 26) )
  30   {
  31     VmHardwareList = (CVmHardware *)CVmConfiguration::getVmHardwareList(this);
  32     Memory = (CVmMemory *)CVmHardware::getMemory(this: VmHardwareList);
  33     if ( (unsigned int)CVmMemory::getRamSize(this: Memory) > 0x2000 )
  34     {
  35       v14 = (CVmHardware *)CVmConfiguration::getVmHardwareList(this);
  36       v15 = (CVmMemory *)CVmHardware::getMemory(this: v14);
  37       CVmMemory::setRamSize(this: v15, a2: 0x2000u);
  38     }
  39     v16 = (CVmHardware *)CVmConfiguration::getVmHardwareList(this);
  40     Cpu = (CVmCpu *)CVmHardware::getCpu(this: v16);
  41     if ( (unsigned int)CVmCpu::getNumber(this: Cpu) >= 5 )
  42     {
  43       v18 = (CVmHardware *)CVmConfiguration::getVmHardwareList(this);
  44       v19 = (CVmCpu *)CVmHardware::getCpu(this: v18);
  45       CVmCpu::setNumber(this: v19, a2: 4u);
  46     }
  47   }
  48   v20 = (CVmSettings *)CVmConfiguration::getVmSettings(this);
  49   VmCommonOptions = (CVmCommonOptions *)CVmSettings::getVmCommonOptions(this: v20);
  50   result = (DisplayUtils *)CVmCommonOptions::getOsVersion(this: VmCommonOptions);
  51   if ( (_DWORD)a1 == 0 && a4 != 0 && ((_DWORD)result == 2067 || (_DWORD)result == 2063) )
  52   {
  53     result = (DisplayUtils *)DisplayUtils::desktopNumScreens(this: result);
  54     if ( (int)result >= 2 )
  55     {
  56       v23 = (CVmHardware *)CVmConfiguration::getVmHardwareList(this);
  57       Video = (CVmVideo *)CVmHardware::getVideo(this: v23);
  58       CVmVideo::setEnableHiResDrawing(this: Video, a2: true);
  59       v25 = (CVmHardware *)CVmConfiguration::getVmHardwareList(this);
  60       v26 = (CVmVideo *)CVmHardware::getVideo(this: v25);
  61       return (DisplayUtils *)CVmVideo::setNativeScalingInGuest(this: v26, a2: true);
  62     }
  63   }
  64   return result;
  65 }
```

```asm
0x1000e85a4 MOV             X0, X22
0x1000e85a8 MOV             W1, #0x1A
0x1000e85ac BL              sub_1000BECA4
0x1000e85b0 TBNZ            W0, #0, loc_1000E860C
0x1000e85b4 MOV             X0, X19; this
0x1000e85b8 BL              CVmConfiguration::getVmHardwareList(void)
0x1000e85bc BL              CVmHardware::getMemory(void)
```

## E15 Linked clone menu gate

Binary `client`, function `0x100507bb8`.

```cpp
     // ... omitted ...
 186     goto LABEL_53;
 187   v21 = *(_DWORD *)(v20 + 4) != 0 ? *(_QWORD *)(a1 + 304) : 0LL;
 188   v22 = (Data *)sub_1000D0BF8(a1: v21);
 189   if ( !sub_1000BECA4(a1: v22, a2: 21) )
 190     goto LABEL_53;
 191   v23 = *(_QWORD *)(a1 + 296);
 192   if ( v23 != 0 && *(_DWORD *)(v23 + 4) != 0 )
 193   {
 194     if ( (sub_1000D22DC(a1: *(_QWORD *)(a1 + 304)) & 1) != 0 )
 195       goto LABEL_53;
     // ... omitted ...
 198   {
 199     goto LABEL_53;
 200   }
 201   QMetaObject::tr(this: (QMetaObject *)&off_101AC6090, a2: "New Linked Clone...", a3: nullptr, a4: -1);
 202   QKeySequence::QKeySequence(this: (QKeySequence *)&v33, a2: 0, a3: 0, a4: 0, a5: 0);
 203   QMenu::addAction(
 204     this: v6,
 205     a2: (const QString *)&v31,
 206     a3: (const QObject *)a1,
 207     a4: "1OnLinkedClone()",
 208     a5: (const QKeySequence *)&v33);
 209   QKeySequence::~QKeySequence(this: (QKeySequence *)&v33);
 210   v25 = (QArrayData *)v31.d.data.l;
 211   if ( *(_DWORD *)v31.d.data.l != -1 )
 212   {
 213     if ( *(_DWORD *)v31.d.data.l != 0 )
```

```asm
0x100508018 BL              sub_1000D0BF8
0x10050801c MOV             W1, #0x15
0x100508020 BL              sub_1000BECA4
0x100508024 CBZ             W0, loc_1005080E4
0x100508028 LDR             X8, [X21,#0x128]
0x10050802c CBZ             X8, loc_100508048
0x100508030 LDR             W8, [X8,#4]
```

## E16 Directional clipboard controls

Binary `client`, function `0x1002c0a4c`.

```cpp
     // ... omitted ...
 123   }
 124 LABEL_30:
 125   v17 = (Data *)sub_100283540(a1: *(_QWORD *)(a1 + 24));
 126   v18 = (QArrayData *)sub_1000BECA4(a1: v17, a2: 46);
 127   if ( (_DWORD)v18 == 0 )
 128     goto LABEL_75;
 129   QMetaObject::tr(this: (QMetaObject *)&QObject::staticMetaObject, a2: "%VM_TYPE% to Mac only", a3: nullptr, a4: -1);
 130   QMetaObject::tr(this: (QMetaObject *)&QObject::staticMetaObject, a2: "%VM_TYPE%", a3: nullptr, a4: -1);
 131   EnumUtils::OsTypeToString(this: v6, a2: v19);
 132   QString::replace(a1: &v37, a2: &v38, a3: &v36, a4: 1);
 133   v21 = (QArrayData *)v36.d.data.l;
 134   if ( *(_DWORD *)v36.d.data.l != -1 )
 135   {
     // ... omitted ...
 175   }
 176 LABEL_48:
 177   QVariant::~QVariant(this: &v36);
 178   QMetaObject::tr(this: (QMetaObject *)&QObject::staticMetaObject, a2: "Mac to %VM_TYPE% only", a3: nullptr, a4: -1);
 179   v26 = v37;
 180   v37 = (QArrayData *)v38.d.data.l;
 181   v38.d.data.l = (signed __int64)v26;
 182   if ( *(_DWORD *)v26 != -1 )
 183   {
 184     if ( *(_DWORD *)v26 != 0 )
```

```asm
0x1002c0cd4 BL              sub_100283540
0x1002c0cd8 MOV             W1, #0x2E ; '.'
0x1002c0cdc BL              sub_1000BECA4
0x1002c0ce0 CBZ             W0, loc_1002C1018
0x1002c0ce4 ADRP            X0, #__ZN7QObject16staticMetaObjectE_ptr@PAGE
0x1002c0ce8 LDR             X0, [X0,#__ZN7QObject16staticMetaObjectE_ptr@PAGEOFF]; this
0x1002c0cec ADRL            X1, aVmTypeToMacOnl; "%VM_TYPE% to Mac only"
0x1002c0cf0 ADRL            X1, aVmTypeToMacOnl; "%VM_TYPE% to Mac only"
```

## E17 Clipboard value normalization

Binary `client`, function `0x1002a2880`.

```cpp
     // ... omitted ...
   1 void __fastcall sub_1002A2880(__int64 a1, QObject *a2, __int64 a3)
   2 {
   3   QComboBox *v5; // x0
   4   QComboBox *v6; // x19
   5   unsigned int v7; // w20
   6   __int64 v8; // x0
   7   int Data; // w20
   8   QVariant v10; // [xsp+10h] [xbp-30h] BYREF
   9
  10   v5 = (QComboBox *)QMetaObject::cast(this: (QMetaObject *)&QComboBox::staticMetaObject, a2);
  11   if ( v5 != nullptr )
  12   {
  13     v6 = v5;
  14     MappingHelpers::getFirstValue(a1: &v10, a2: a3);
  15     v7 = QVariant::toLongLong(this: &v10, a2: nullptr);
  16     QVariant::~QVariant(this: &v10);
  17     v8 = sub_100283540(a1: *(_QWORD *)(a1 + 24));
  18     if ( (sub_1000BECA4(a1: v8, a2: 46) & 1) == 0 && (v7 & 0xFFFFFFFE) == 2 )
  19     {
  20       if ( dword_101B448D8 >= 1 )
  21         sub_10072D89C(
  22           a1: "",
  23           a2: "prl_client_app",
  24           a3: 1,
  25           a4: "Unidirectional CP mode: %d is not supported by license type",
  26           v7);
  27       v7 = 1;
  28     }
  29     QVariant::QVariant(this: &v10, a2: v7);
  30     Data = QComboBox::findData(a1: v6, a2: &v10, a3: 256, a4: 16);
  31     QVariant::~QVariant(this: &v10);
  32     if ( (Data & 0x80000000) == 0 )
  33       QComboBox::setCurrentIndex(this: v6, a2: Data);
  34   }
  35 }
```

```asm
0x1002a28dc MOV             W1, #0x2E ; '.'
0x1002a28e0 BL              sub_1000BECA4
0x1002a28e4 TBNZ            W0, #0, loc_1002A2930
0x1002a28e8 AND             W8, W20, #0xFFFFFFFE
0x1002a28ec CMP             W8, #2
0x1002a28f0 B.NE            loc_1002A2930
```

## E18 SDK feature entry

Binary `sdk`, function `0x31c40`.

```cpp
     // ... omitted ...
   1 __int64 __fastcall PrlSrv_IsFeatureSupported(__int64 a1, int a2, __int64 a3)
   2 {
   3   __int64 v4; // x19
   4   __int64 v6; // [xsp+0h] [xbp-20h] BYREF
   5   int v7; // [xsp+Ch] [xbp-14h] BYREF
   6
   7   v7 = a2;
   8   v6 = a3;
   9   sub_9444(a1);
  10   v4 = sub_3BBF8(a1, a2: sub_47434, a3: 0, a4: &v7, a5: &v6);
  11   sub_9484();
  12   return v4;
  13 }
```

```asm
0x31c40 SUB             SP, SP, #0x30
0x31c44 STP             X20, X19, [SP,#0x20+var_10]
0x31c48 STP             X29, X30, [SP,#0x20+var_s0]
0x31c4c ADD             X29, SP, #0x20
0x31c50 MOV             X19, X0
0x31c54 STR             W1, [SP,#0x20+var_14]
0x31c58 STR             X2, [SP,#0x20+var_20]
0x31c5c BL              sub_9444
0x31c60 ADRL            X1, sub_47434
0x31c64 ADRL            X1, sub_47434
0x31c68 ADD             X3, SP, #0x20+var_14
0x31c6c MOV             X4, SP
0x31c70 MOV             X0, X19
0x31c74 MOV             X2, #0
0x31c78 BL              sub_3BBF8
0x31c7c MOV             X19, X0
0x31c80 BL              sub_9484
0x31c84 MOV             X0, X19
0x31c88 LDP             X29, X30, [SP,#0x20+var_s0]
0x31c8c LDP             X20, X19, [SP,#0x20+var_10]
0x31c90 ADD             SP, SP, #0x30 ; '0'
0x31c94 RET
```

## E19 SDK feature query

Binary `sdk`, function `0x47434`.

```cpp
     // ... omitted ...
   1 __int64 __fastcall sub_47434(__int64 a1, __int64 a2, _DWORD *a3)
   2 {
   3   __int64 v6; // x19
   4
   5   v6 = a1 + 88;
   6   QMutex::lock(this: (QMutex *)(a1 + 88));
   7   *a3 = sub_18F488(a1: a1 + 176, a2);
   8   QMutex::unlock(this: (QMutex *)(v6 & 0xFFFFFFFFFFFFFFFELL));
   9   return 0;
  10 }
```

```asm
0x47434 STP             X22, X21, [SP,#-0x10+var_20]!
0x47438 STP             X20, X19, [SP,#0x20+var_10]
0x4743c STP             X29, X30, [SP,#0x20+var_s0]
0x47440 ADD             X29, SP, #0x20
0x47444 MOV             X20, X2
0x47448 MOV             X21, X1
0x4744c MOV             X22, X0
0x47450 ADD             X19, X0, #0x58 ; 'X'
0x47454 MOV             X0, X19; this
0x47458 BL              QMutex::lock(void)
0x4745c ADD             X0, X22, #0xB0
0x47460 MOV             X1, X21
0x47464 BL              sub_18F488
0x47468 STR             W0, [X20]
0x4746c AND             X0, X19, #0xFFFFFFFFFFFFFFFE; this
0x47470 BL              QMutex::unlock(void)
0x47474 MOV             W0, #0
0x47478 LDP             X29, X30, [SP,#0x20+var_s0]
0x4747c LDP             X20, X19, [SP,#0x20+var_10]
0x47480 LDP             X22, X21, [SP+0x20+var_20],#0x30
0x47484 RET
```

## E20 SDK feature membership

Binary `sdk`, function `0x18f488`.

```cpp
     // ... omitted ...
   1 bool __fastcall sub_18F488(__int64 *a1, int a2)
   2 {
   3   __int64 *v2; // x8
   4   unsigned int v3; // w9
   5   unsigned int v4; // w10
   6   __int64 *i; // x9
   7
   8   v2 = (__int64 *)*a1;
   9   v3 = *(_DWORD *)(*a1 + 32);
  10   if ( v3 != 0 )
  11   {
  12     v4 = *((_DWORD *)v2 + 9) ^ a2;
  13     for ( i = *(__int64 **)(v2[1] + 8LL * (v4 % v3)); i != v2; i = (__int64 *)*i )
  14     {
  15       if ( *((_DWORD *)i + 2) == v4 && *((_DWORD *)i + 3) == a2 )
  16         return i != v2;
  17     }
  18   }
  19   i = (__int64 *)*a1;
  20   return i != v2;
  21 }
```

```asm
0x18f488 LDR             X8, [X0]
0x18f48c LDR             W9, [X8,#0x20]
0x18f490 CBZ             W9, loc_18F4D8
0x18f494 LDR             W10, [X8,#0x24]
0x18f498 EOR             W10, W10, W1
0x18f49c LDR             X11, [X8,#8]
0x18f4a0 UDIV            W12, W10, W9
0x18f4a4 MSUB            W9, W12, W9, W10
0x18f4a8 LDR             X9, [X11,W9,UXTW#3]
0x18f4ac B               loc_18F4B4
0x18f4b0 LDR             X9, [X9]
0x18f4b4 CMP             X9, X8
0x18f4b8 B.EQ            loc_18F4D8
0x18f4bc LDR             W11, [X9,#8]
0x18f4c0 CMP             W11, W10
0x18f4c4 B.NE            loc_18F4B0
0x18f4c8 LDR             W11, [X9,#0xC]
0x18f4cc CMP             W11, W1
0x18f4d0 B.NE            loc_18F4B0
0x18f4d4 B               loc_18F4DC
0x18f4d8 MOV             X9, X8
0x18f4dc CMP             X9, X8
0x18f4e0 CSET            W0, NE
0x18f4e4 RET
```