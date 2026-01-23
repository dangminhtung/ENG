/*
? Please tell me n detail which bell tower you like and who is your favorite singer

I don’t remember exactly when I first started listening to music. When I was in middle school, my parents bought me an MP3 player, and I often listened to many songs on it. One day, I heard a song called “Lie” by Big Bang, a famous K-pop group. The song had a lively melody and touching lyrics, so I became a big fan of K-pop. Even now, I enjoy listening to K-pop before going to bed because it helps me relax and feel good.

I dont remember exactly when i first started listening to music. when i was in middle school, my parents bought me an mp3 player, and i often listened t many songs on it . one day, i heard a song called lie by big bang, a famous kpop group. the song had a lively melody and touching lyrics , so i became a big fan of kpop even now, i enjoy listeniong to kpop before going to ed because it helps me relax and feel good

? Who listens to music with you for the first time and where do you listen to music


I don’t remember exactly when I first started listening to music. When I was in middle school, my parents bought me an MP3 player, and I heard “Lie” by Big Bang, a famous K-pop group. The song had touching lyrics and a lively melody, so I became a big fan of K-pop. Now I often listen to music to relax and relieve stress. I usually use headphones because they block outside noise very well.

? Please tell me more about how to listen to muisc

* Whenever I have free time, I enjoy listening to fast pop music. At home, I use my computer with a good audio system, so the sound is great and makes me feel like I’m in a club. When I go out, I usually listen to music on my smartphone with headphones, which helps me concentrate. It’s very convenient because I can listen anytime and anywhere.

Bất cứ khi nào rảnh rỗi, tôi thích nghe nhạc pop sôi động. Ở nhà, tôi dùng máy tính với dàn âm thanh tốt nên âm thanh rất tuyệt, khiến tôi có cảm giác như đang ở trong một câu lạc bộ. Khi ra ngoài, tôi thường nghe nhạc trên điện thoại thông minh bằng tai nghe, giúp tôi tập trung hơn. Điều này rất tiện lợi vì tôi có thể nghe mọi lúc mọi nơi.


? Change


I love listening to music. When I was young, I liked fast songs like K-pop because they made me feel excited. But when I entered high school, I started to enjoy ballads because my friend always listened to them. Ballad songs make me feel calm and help me relax after a long day. These days, I like to listen to calm music in the morning to start my day peacefully.


GBL architeecture

Trên nền tảng Qualcomm:

PBL (Primary Bootloader) nằm trong ROM.

PBL nạp SBL1, rồi SBL1 nạp SBL2, và sau đó là GBL hoặc XBL (eXtensible BootLoader).

GBL/XBL chịu trách nhiệm:

Xác minh ABL/LK.

Nạp các partition như boot, vbmeta, dtbo.

Chuẩn bị Device Tree, Verified Boot chain.

Ở các máy dùng UEFI boot (như Windows ARM), GBL chuyển quyền điều khiển sang UEFI DXE core thay vì Android Bootloader.


+-----------------------------------------------------------+
|                     Power On / Reset                      |
+-----------------------------------------------------------+
                              │
                              ▼
┌───────────────────────────────────────────────────────────┐
│ [1] ROM Code / PBL (Primary Boot Loader)                  │
│  • Nằm trong ROM của SoC (không thể thay đổi)             │
│  • Xác minh chữ ký của SBL1 bằng khóa Root-of-Trust       │
│  • Nạp SBL1 từ eMMC/UFS                                   │
└───────────────────────────────────────────────────────────┘
                              │
                              ▼
┌───────────────────────────────────────────────────────────┐
│ [2] SBL1 / XBL Loader (Secondary Boot Loader)             │
│  • Khởi tạo bộ nhớ DRAM, nguồn, xung nhịp                 │
│  • Nạp các thành phần TrustZone / TEE                     │
│  • Xác minh và nạp GBL                                    │
└───────────────────────────────────────────────────────────┘
                              │
                              ▼
┌───────────────────────────────────────────────────────────┐
│ [3] GBL (Generic Boot Loader)                             │
│  • Tầng trung gian giữa SBL và bootloader OS              │
│  • Xác minh chữ ký của UEFI / ABL                         │
│  • Cấu hình môi trường pre-boot (RAM map, device info)    │
│  • Có thể cung cấp fastboot/download mode                 │
│  • Nếu hệ thống hỗ trợ UEFI → GBL nạp DXE Core (UEFI)     │
└───────────────────────────────────────────────────────────┘
                              │
                              ▼
┌───────────────────────────────────────────────────────────┐
│ [4] UEFI Firmware                                         │
│  • DXE phase: nạp driver, protocol, service               │
│  • BDS phase: chọn thiết bị boot (boot.img, ESP, GRUB…)   │
│  • Giao diện chuẩn (EFI Protocols)                        │
│  • Xác minh chữ ký OS loader (Secure Boot)                │
└───────────────────────────────────────────────────────────┘
                              │
                              ▼
┌───────────────────────────────────────────────────────────┐
│ [5] ABL / LK / GRUB (Android Boot Loader / OS Loader)     │
│  • Nạp boot.img (kernel + ramdisk + DTB)                  │
│  • Truyền thông tin boot qua bootargs                     │
│  • Kích hoạt Verified Boot (vbmeta)                       │
└───────────────────────────────────────────────────────────┘
                              │
                              ▼
┌───────────────────────────────────────────────────────────┐
│ [6] Kernel + Initramfs                                    │
│  • Kernel khởi tạo thiết bị, mount file system            │
│  • dm-verity kiểm tra tính toàn vẹn / AVB                 │
│  • Chạy init → khởi động Android Framework                │
└───────────────────────────────────────────────────────────┘


 ┌────────────────────────────────────────────────────────────┐
 │                 Qualcomm Secure Boot Chain                 │
 └────────────────────────────────────────────────────────────┘

        ┌────────────────────────────────────────────┐
        │ Hardware Root-of-Trust (eFuse/QFuse keys)  │
        └────────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────┐
│  PBL (Primary Boot Loader - in ROM)                        │
│  - Đọc SBL/XBL từ flash                                    │
│  - Xác minh chữ ký bằng OEM Root Key (fused key)           │
│  - Nếu hợp lệ → nạp vào RAM và chạy                        │
└────────────────────────────────────────────────────────────┘
                          │
         (verify using OEM Root Key)
                          ▼
┌────────────────────────────────────────────────────────────┐
│  SBL / XBL (Secondary Boot Loader)                         │
│  - Thiết lập DRAM, peripheral                              │
│  - Xác minh các firmware quan trọng:                       │
│      • tz.mbn (TrustZone)                                  │
│      • rpm.mbn (Power Manager)                             │
│      • hyp.mbn (Hypervisor)                                │
│  - Xác minh và nạp GBL                                      │
│  - Dùng Secondary Boot Key (SBK)                           │
└────────────────────────────────────────────────────────────┘
                          │
         (verify using Secondary Boot Key)
                          ▼
┌────────────────────────────────────────────────────────────┐
│  GBL (Generic BootLoader)                                  │
│  - Xác minh nhiều image firmware khác:                     │
│      • abl.elf / uefi.elf (Android Bootloader)             │
│      • modem.mbn (Baseband)                                │
│      • dspso.mbn (DSP firmware)                            │
│      • tz.mbn / hyp.mbn nếu chưa có                        │
│  - Kiểm tra rollback index                                 │
│  - Thiết lập secure context, chuyển sang ABL               │
│  - Dùng Generic Boot Key (GBK)                             │
└────────────────────────────────────────────────────────────┘
                          │
         (verify using Generic Boot Key)
                          ▼
┌────────────────────────────────────────────────────────────┐
│  ABL / UEFI                                                │
│  - Bắt đầu phần "Android Verified Boot"                    │
│  - Load vbmeta partition                                   │
│  - Dùng AVB public key để xác minh:                        │
│      • vbmeta.img                                          │
│      • boot.img, dtbo.img, vendor.img, system.img           │
│  - Nếu tất cả hợp lệ → nạp kernel                          │
└────────────────────────────────────────────────────────────┘
                          │
         (verify using AVB Key)
                          ▼
┌────────────────────────────────────────────────────────────┐
│  Android Kernel + dm-verity                                │
│  - Xác minh hash block-level của /system, /vendor...        │
│  - Đảm bảo integrity suốt runtime                          │
└────────────────────────────────────────────────────────────┘

*/