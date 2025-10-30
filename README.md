# منظف النظام الذكي (Smart System Cleaner)
تحذير لطيف: لن يُحذف أي شيء حساس بدون موافقتك الصريحة.
---
##  تشغيل المشروع محلياً
- المتطلبات: Python 3.9+ أو Node.js 18+
خيار Python:
```
python3 -m venv .venv
source .venv/bin/activate   # على ويندوز: .venv\Scripts\activate
pip install -r requirements.txt  # إن وُجد
python main.py --mode fast --dry-run
```
خيار Node.js:
```
node index.js --mode fast --dry-run
```
- يمكن تمرير معاملات:
  
- --mode [
fast|deep|custom
]
  
- --dry-run لمعاينة النتائج دون حذف
  
- --paths لتحديد مجلدات إضافية
  
- --exclude لاستثناء أنماط معيّنة
---
##  بنية المشروع
```
Smart-System-Cleaner/
├─ screenshots/
│  ├─ image.jpg                 # الرسم التوضيحي المرفق
│  ├─ ui_mock_arabic.png        # واجهة افتراضية
│  └─ cleanup_report.png        # تقرير افتراضي بالنتائج
├─ main.py                      # تخطيط أولي بلغة بايثون
├─ index.js                     # تخطيط بديل بجافاسكربت
├─ LICENSE                      # رخصة MIT
└─ README.md                    # هذا الملف
```
---
##  خارطة الطريق (Roadmap)
- إضافة واجهة رسومية فعلية ببايثون (PySide6/Qt) أو Electron.
- تكامل مع مكتبات الرسم البياني (matplotlib/plotly أو chart.js) لعرض النتائج.
- وحدة ذكاء بسيطة لتعلّم أنماط الاستخدام واقتراح تنظيفات مستقبلية.
- دعم جدولة التنظيف التلقائي وإشعارات قبل/بعد التنفيذ.
---
##  أدوات بديلة مشهورة لتنظيف وتحسين النظام:
| اسم الأداة | الوظيفة | الرابط |
|------------|---------|--------|
| CCleaner | تنظيف الملفات المؤقتة وتحسين أداء النظام | [https://www.ccleaner.com](https://www.ccleaner.com) |
| BleachBit | تنظيف ملفات النظام غير المستخدمة وحذف البيانات الحساسة بشكل آمن | [https://bleachbit.net](https://bleachbit.net) |
| Wise Disk Cleaner | تنظيف الملفات المؤقتة والغير ضرورية وتحسين أداء القرص الصلب | [https://wise-disk-cleaner.pages.dev](https://wise-disk-cleaner.pages.dev) |
| Glary Utilities | مجموعة من الأدوات لتنظيف الجهاز وإصلاح الأخطاء وتحسين الأداء | [https://glaryutilities.org](https://glaryutilities.org) |
| Avast Cleanup | تنظيف الجهاز من الملفات الغير ضرورية وإصلاح الأخطاء في السجل | [https://www.avast.com/en-ae/cleanup](https://www.avast.com/en-ae/cleanup) |
| IObit Advanced SystemCare | تنظيف الجهاز وتحسين أداء النظام وحمايته من البرامج الضارة | [https://www.iobit.com/en/advancedcare.php](https://www.iobit.com/en/advancedcare.php) |
| Ashampoo WinOptimizer | تنظيف الجهاز وإصلاح الأخطاء في النظام وتحسين أداء الجهاز | [https://www.ashampoo.com/en-usd/winoptimizer](https://www.ashampoo.com/en-usd/winoptimizer) |
| Windows Disk Cleanup | أداة مدمجة في ويندوز لتنظيف الملفات المؤقتة والغير ضرورية | [https://support.microsoft.com/en-us/windows/free-up-drive-space-in-windows-85529ccb-c365-490d-b548-831022bc9b32](https://support.microsoft.com/en-us/windows/free-up-drive-space-in-windows-85529ccb-c365-490d-b548-831022bc9b32) |
| Privacy Eraser | مسح البيانات الشخصية وتنظيف آثار التصفح على الإنترنت بشكل آمن | [https://www.privacyeraser.com](https://www.privacyeraser.com) |
| PC Decrapifier | إزالة البرامج الغير ضرورية والتطبيقات المثبتة مسبقاً | [https://pc-decrapifier.updatestar.com](https://pc-decrapifier.updatestar.com) |
| JetClean | تنظيف الجهاز وتحسين أداء النظام وتحرير مساحة القرص الصلب | [https://jetclean.en.filerox.com](https://jetclean.en.filerox.com) |
| SlimCleaner | تنظيف الجهاز وإدارة البرامج المثبتة وتحسين أداء النظام | [https://slimcleaner.updatestar.com/en](https://slimcleaner.updatestar.com/en) |
| DiskMax | تنظيف الجهاز وتحسين أداء القرص الصلب وإصلاح الأخطاء | [https://diskmax.en.lo4d.com/windows](https://diskmax.en.lo4d.com/windows) |
| Auslogics Disk Defrag | تنظيم ملفات القرص الصلب وتحسين أداء الجهاز | [https://filehippo.com/download_auslogics-disk-defrag/](https://filehippo.com/download_auslogics-disk-defrag/) |
| Windows Repair Toolbox | إصلاح الأخطاء في النظام وتنظيف الجهاز وتحسين أداء النظام | [https://windows-repair-toolbox.com](https://windows-repair-toolbox.com) |
| TuneUp Utilities | تنظيف الجهاز وإصلاح الأخطاء في النظام وتحسين أداء الجهاز | [https://www.avg.com/en-ww/avg-pctuneup](https://www.avg.com/en-ww/avg-pctuneup) |
| Comodo System Utilities | تنظيف الجهاز وتحسين أداء النظام وحمايته من البرامج الضارة | [https://www.comodo.com/home/support-maintenance/system-utilities.php](https://www.comodo.com/home/support-maintenance/system-utilities.php) |
| PC Cleaner Pro | تنظيف الجهاز وتحسين أداء النظام وتسريع الإنترنت | [https://www.pccleanerpro.com](https://www.pccleanerpro.com) |
| System Mechanic | تنظيف الجهاز وإصلاح الأخطاء في النظام وتحسين أداء الجهاز | [https://www.iolo.com/products/system-mechanic/](https://www.iolo.com/products/system-mechanic/) |
| Kaspersky PC Cleaner | تنظيف الجهاز وإزالة الملفات الغير ضرورية وتحسين أداء النظام | [https://www.kaspersky.com/free-pc-cleaner](https://www.kaspersky.com/free-pc-cleaner) |
| Disk Cleaner | تنظيف القرص الصلب وتحسين أداء الجهاز وإزالة الملفات الغير ضرورية | [https://diskcleaner.net](https://diskcleaner.net) |
| Total PC Cleaner | تنظيف الجهاز وتحسين أداء النظام وإزالة الملفات الغير ضرورية | [https://www.totalpccleaner.com/](https://www.totalpccleaner.com/) |
| AdwCleaner | إزالة البرامج الإعلانية غير المرغوب فيها والبرامج الضارة من الجهاز | [https://www.malwarebytes.com/adwcleaner](https://www.malwarebytes.com/adwcleaner) |
| Norton Utilities | تنظيف الجهاز وإصلاح الأخطاء في النظام وتحسين أداء الجهاز | [https://us.norton.com/products/norton-utilities](https://us.norton.com/products/norton-utilities) |
| PC Health Advisor | تنظيف الجهاز وإصلاح الأخطاء في النظام وتحسين أداء الجهاز | [https://www.pchealthadvisor.com](https://www.pchealthadvisor.com) |
| Clean Master for PC | تنظيف الجهاز وتحسين أداء النظام وتسريع الكمبيوتر | [https://www.cleanmasterofficial.com/pc/](https://www.cleanmasterofficial.com/pc/) |
| System Ninja | تنظيف الجهاز وإزالة الملفات الغير ضرورية وتحسين الأداء | [https://singularabs.com/software/system-ninja/](https://singularabs.com/software/system-ninja/) |

---
## أوامر Batch المتقدمة لتنظيف النظام
| رقم الأمر | الوظيفة | الأمر البرمجي | رابط أو مصدر إذا وجد |
|---|---|---|---|
| 1 | حذف الملفات المؤقتة للمستخدم | `del /s /q /f %temp%\*` | [oktechmasters](https://oktechmasters.org/ar/%D9%86%D9%88%D8%A7%D9%81%D8%B0/%D9%85%D8%B3%D8%AD-%D8%B0%D8%A7%D9%83%D8%B1%D8%A9-%D8%A7%D9%84%D8%AA%D8%AE%D8%B2%D9%8A%D9%86-%D8%A7%D9%84%D9%85%D8%A4%D9%82%D8%AA/) |
| 2 | حذف ملفات النظام المؤقتة | `del /s /q /f %systemroot%\temp\*` |  |
| 3 | مسح كاش Internet Explorer | `RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 8` | |
| 4 | مسح كاش تحديثات ويندوز | ```bat
net stop wuauserv
rmdir /s /q %windir%\SoftwareDistribution
net start wuauserv
``` | [microsoft](https://support.microsoft.com/ar-sa/windows/%D8%AA%D9%84%D9%85%D9%8A%D8%AD%D8%A7%D8%AA-%D9%84%D8%AA%D8%AD%D8%B3%D9%8A%D9%86-%D8%A3%D8%AF%D8%A7%D8%A1-%D8%A7%D9%84%D9%83%D9%85%D8%A8%D9%8A%D9%88%D8%AA%D8%B1-%D9%81%D9%8A-windows-b3b3ef5b-5953-fb6a-2528-4bbed82fba96) |
| 5 | تنظيف المثبتات القديمة | `msizap.exe g!` |  |
| 6 | حذف Prefetch | `del /q /s /f %windir%\prefetch\*` |  |
| 7 | تعطيل الهيبرنيشن | `powercfg -h off` | [microsoft](https://support.microsoft.com/ar-sa/windows/%D8%AA%D9%84%D9%85%D9%8A%D8%AD%D8%A7%D8%AA-%D9%84%D8%AA%D8%AD%D8%B3%D9%8A%D9%86-%D8%A3%D8%AF%D8%A7%D8%A1-%D8%A7%D9%84%D9%83%D9%85%D8%A8%D9%8A%D9%88%D8%AA%D8%B1-%D9%81%D9%8A-windows-b3b3ef5b-5953-fb6a-2528-4bbed82fba96) |
| 8 | حذف كاش الصور المصغرة | `del /q /s /f /a:h %localappdata%\Microsoft\Windows\Explorer\thumbcache_*.db` |  |
| 9 | مسح DNS كاش | `ipconfig /flushdns` | [arabitec](https://arabitec.com/%D8%AA%D9%86%D8%B8%D9%8A%D9%81-%D9%83%D8%A7%D8%B4-%D8%A7%D9%84%D9%88%D9%8A%D9%86%D8%AF%D9%88%D8%B2/) |
| 10 | تنظيف سجل الأحداث Event Logs | `wevtutil el | Foreach-Object {wevtutil cl "$"}` | [microsoft](https://support.microsoft.com/ar-sa/windows/%D8%AA%D9%84%D9%85%D9%8A%D8%AD%D8%A7%D8%AA-%D9%84%D8%AA%D8%AD%D8%B3%D9%8A%D9%86-%D8%A3%D8%AF%D8%A7%D8%A1-%D8%A7%D9%84%D9%83%D9%85%D8%A8%D9%8A%D9%88%D8%AA%D8%B1-%D9%81%D9%8A-windows-b3b3ef5b-5953-fb6a-2528-4bbed82fba96) |
| 11 | حذف ملفات الإنترنت المؤقتة | `del /q /s /f "%userprofile%\AppData\Local\Microsoft\Windows\Temporary Internet Files\*.*"` |  |
| 12 | حذف Windows.old بعد الترقية | `rd /s /q %SystemDrive%\windows.old` | [microsoft](https://support.microsoft.com/ar-sa/windows/%D8%AA%D9%84%D9%85%D9%8A%D8%AD%D8%A7%D8%AA-%D9%84%D8%AA%D8%AD%D8%B3%D9%8A%D9%86-%D8%A3%D8%AF%D8%A7%D8%A1-%D8%A7%D9%84%D9%83%D9%85%D8%A8%D9%8A%D9%88%D8%AA%D8%B1-%D9%81%D9%8A-windows-b3b3ef5b-5953-fb6a-2528-4bbed82fba96) |
| 13 | تنظيف بقايا تحديثات النظام | `dism.exe /Online /Cleanup-Image /StartComponentCleanup /ResetBase` |  |
| 14 | حذف كاش متجر Windows | `wsreset.exe` | [youstable](https://www.youstable.com/ar/blog/clear-cache-in-windows-11/) |
| 15 | تفريغ سلة المحذوفات | `rd /s /q %SystemDrive%\$Recycle.bin` |  |
| 16 | تنظيف سجلات النظام (PowerShell) | `for /F "tokens=*" %1 in ('wevtutil.exe el') DO wevtutil.exe cl "%1"` |  |
| 17 | حذف Windows.old بصلاحيات مسؤول | ```bat
takeown /F %SystemDrive%\windows.old /R /A /D Y
icacls %SystemDrive%\windows.old /grant administrators:F /T
rd /S /Q %SystemDrive%\windows.old
``` | [microsoft](https://support.microsoft.com/ar-sa/windows/%D8%AA%D9%84%D9%85%D9%8A%D8%AD%D8%A7%D8%AA-%D9%84%D8%AA%D8%AD%D8%B3%D9%8A%D9%86-%D8%A3%D8%AF%D8%A7%D8%A1-%D8%A7%D9%84%D9%83%D9%85%D8%A8%D9%8A%D9%88%D8%AA%D8%B1-%D9%81%D9%8A-windows-b3b3ef5b-5953-fb6a-2528-4bbed82fba96) |
| 18 | تعطيل السبات (صيغة أخرى) | `powercfg.exe /hibernate off` |  |
| 19 | حذف نقاط استعادة النظام | `vssadmin delete shadows /for=%systemdrive% /all /quiet` |  |
| 20 | تنظيف كاش Microsoft Edge | `del /F /Q /A:R %LocalAppData%\Packages\Microsoft.MicrosoftEdge*\AC\INetCache\*.*` | [youstable](https://www.youstable.com/ar/blog/clear-cache-in-windows-11/) |
| 21 | مسح تاريخ البحث في ويندوز | `del /q /s /f %localappdata%\Microsoft\Windows\ConnectedSearch\*` |  |
| 22 | حذف ملفات LogFiles | `del /q /s /f %SystemRoot%\System32\LogFiles\*.*` |  |
| 23 | تنظيف سجلات النظام (تكرار) | `for /F "tokens=*" %1 in ('wevtutil.exe el') DO wevtutil.exe cl "%1"` |  |
| 24 | حذف تقارير أخطاء ويندوز | `del /s /q /f %localappdata%\Microsoft\Windows\WER\*` |  |
| 25 | تنظيف كاش Windows Defender | `del /q /s /f %ProgramData%\Microsoft\Windows Defender\Scans\*` |  |
