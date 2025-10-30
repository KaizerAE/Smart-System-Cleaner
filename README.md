# منظف النظام الذكي (Smart System Cleaner)
---
## أوامر Batch المتقدمة لتنظيف النظام
تنسيق العرض: لكل أمر عنوان فرعي، يليه مربع كود PowerShell يحتوي الصيغة التنفيذية المباشرة (irm "URL" | iex) إن وُجد، أو كود الأوامر ككتلة. أسفل كل أمر وصف مختصر بالعربية يوضح وظيفته والتنبيه إلى الحاجة لصلاحيات المسؤول إذا لزم.

#### Stable Branch (موصى به)
```powershell
irm "https://christitus.com/win" | iex
```
- هذا أمر مباشر يجلب سكريبت ضبط وتنظيف ويندوز من المصدر الرسمي ويشغله فوراً عبر PowerShell. يفضّل تشغيله كمسؤول لضمان تطبيق جميع التعديلات.

#### Dev Branch (للتجربة والتطوير)
```powershell
irm "https://christitus.com/windev" | iex
```
- هذا أمر مباشر للنسخة التطويرية ويحتوي تغييرات تجريبية. يُنصح به للمستخدمين المتقدمين ومع تشغيل نافذة PowerShell كمسؤول.

---

#### حذف الملفات المؤقتة للمستخدم
```bat
del /s /q /f %temp%\*
```
- يحذف ملفات الكاش المؤقتة لحساب المستخدم لتفريغ مساحة وتحسين الأداء. قد يغلق بعض التطبيقات المؤقتة المفتوحة ملفاتها تلقائياً.

#### حذف ملفات النظام المؤقتة
```bat
del /s /q /f %systemroot%\temp\*
```
- يزيل الملفات المؤقتة على مستوى النظام. يُفضّل تشغيل موجه الأوامر كمسؤول لضمان حذف جميع العناصر.

#### مسح كاش Internet Explorer
```bat
RunDll32.exe InetCpl.cpl,ClearMyTracksByProcess 8
```
- يمسح ذاكرة التخزين المؤقتة للمتصفح الموروث IE لتحرير مساحة وحل بعض مشاكل التصفح القديمة.

#### مسح كاش تحديثات ويندوز (Windows Update Cache)
```bat
net stop wuauserv
rmdir /s /q %windir%\SoftwareDistribution
net start wuauserv
```
- يعيد إنشاء مجلد تحديثات ويندوز لحل علَق التحديثات أو تسريعها. يتطلب نافذة بمستوى مسؤول.

#### تنظيف المثبتات القديمة (Windows Installer)
```bat
msizap.exe g!
```
- يحذف بقايا حزم المثبت (MSI) القديمة لتقليل المساحة المهدورة. ينصح باستخدامه بحذر ومع صلاحيات مسؤول.

#### حذف Prefetch
```bat
del /q /s /f %windir%\prefetch\*
```
- يفرغ ملفات Prefetch لإجبار النظام على إعادة توليدها. قد يبطئ الإقلاع الأولي بعد التنظيف بشكل مؤقت.

#### تعطيل الهيبرنيشن (Hibernate)
```bat
powercfg -h off
```
- يعطل السبات ويوفر مساحة تعادل حجم ملف hiberfil.sys. يحتاج موجه أوامر/PowerShell بصلاحيات مسؤول.

#### حذف كاش الصور المصغّرة (Thumbnails)
```bat
del /q /s /f /a:h %localappdata%\Microsoft\Windows\Explorer\thumbcache_*.db
```
- يحذف قواعد بيانات المصغرات لحل مشاكل عرض الأيقونات القديمة وإعادة توليدها تلقائياً.

#### مسح DNS Cache
```bat
ipconfig /flushdns
```
- يمسح كاش DNS لإصلاح مشاكل الدومينات أو التوجيه الشبكي.

#### إعادة تعيين كاش متجر Microsoft Store
```bat
wsreset.exe
```
- يعيد تهيئة كاش المتجر لحل مشاكل التحميل أو التحديثات فيه.

#### تفريغ سلة المحذوفات
```bat
rd /s /q %SystemDrive%\$Recycle.bin
```
- يحذف محتوى سلة المحذوفات لجميع المستخدمين على القرص النظام. يتطلب عادة صلاحيات مسؤول.

#### تنظيف سجلات النظام (صيغة أوامر دفعية)
```bat
for /F "tokens=*" %%i in ('wevtutil.exe el') do wevtutil.exe cl "%%i"
```
- بديل دفعي لمسح جميع سجلات الأحداث، مناسب للتشغيل داخل ملفات .bat كمسؤول.

#### حذف Windows.old بصلاحيات مسؤول (قوي)
```bat
takeown /F %SystemDrive%\windows.old /R /A /D Y
icacls %SystemDrive%\windows.old /grant administrators:F /T
rd /S /Q %SystemDrive%\windows.old
```
- يستحوذ على الأذونات ثم يحذف المجلد بالكامل في حال فشل الحذف السريع. يتطلب نافذة مسؤول.

#### تعطيل السبات (صيغة بديلة)
```bat
powercfg.exe /hibernate off
```
- صيغة مكافئة لتعطيل السبات وتحرير مساحة hiberfil.sys.

#### حذف نقاط استعادة النظام
```bat
vssadmin delete shadows /for=%systemdrive% /all /quiet
```
- يحذف جميع نقاط الاستعادة لتحرير مساحة كبيرة. تحذير: لا يمكن التراجع؛ استخدم بحذر وبصلاحيات مسؤول.

#### تنظيف كاش Microsoft Edge (UWP)
```bat
del /F /Q /A:R %LocalAppData%\Packages\Microsoft.MicrosoftEdge*\AC\INetCache\*.*
```
- يزيل كاش المتصفح القديم لإصلاح مشاكل التصفح أو المساحة. قد تتطلب بعض المسارات صلاحيات.

#### مسح تاريخ البحث في ويندوز
```bat
del /q /s /f %localappdata%\Microsoft\Windows\ConnectedSearch\*
```
- يحذف محفوظات البحث المحلية لواجهة ويندوز Search.

#### حذف ملفات LogFiles
```bat
del /q /s /f %SystemRoot%\System32\LogFiles\*.*
```
- يزيل سجلات متنوعة غير ضرورية لتقليل استهلاك المساحة. يُفضل التشغيل كمسؤول.

#### حذف تقارير أخطاء ويندوز (WER)
```bat
del /s /q /f %localappdata%\Microsoft\Windows\WER\*
```
- يحذف ملفات تقارير الأخطاء المرسلة/المعلقة لتخفيف الحجم.

#### تنظيف كاش Windows Defender (سجلات الفحص)
```bat
del /q /s /f "%ProgramData%\Microsoft\Windows Defender\Scans\*"
```
- يحذف سجلات وكاش الفحوصات القديمة لـ Microsoft Defender لتحرير المساحة.

---

### ملاحظات:
- بعض الأوامر قد تُغلق عمليات أو خدمات وتحتاج إعادة تشغيل الجهاز للحصول على أفضل نتيجة.
- الأوامر التي تؤثر على التحديثات، السبات، نقاط الاستعادة أو مجلدات النظام تتطلب نافذة موجه أوامر/PowerShell كمسؤول.

---

## أدوات تنظيف بديلة ومشهورة

| الأداة | الوصف | الرابط |
|--------|-------|--------|
| **CCleaner** | أداة شهيرة لتنظيف الملفات المؤقتة والريجستري وإدارة برامج بدء التشغيل. | [تحميل CCleaner](https://www.ccleaner.com/) |
| **BleachBit** | أداة مجانية ومفتوحة المصدر لتنظيف النظام وحماية الخصوصية. | [تحميل BleachBit](https://www.bleachbit.org/) |
| **Wise Disk Cleaner** | أداة سريعة وآمنة لتنظيف القرص الصلب وإزالة الملفات غير الضرورية. | [تحميل Wise Disk Cleaner](https://www.wisecleaner.com/wise-disk-cleaner.html) |
| **Glary Utilities** | مجموعة أدوات شاملة لصيانة النظام وتحسين الأداء. | [تحميل Glary Utilities](https://www.glarysoft.com/) |
| **System Ninja** | أداة خفيفة وسريعة لتنظيف النظام وإزالة الملفات غير المرغوب فيها. | [تحميل System Ninja](https://singularlabs.com/software/system-ninja/) |
| **Windows Disk Cleanup** | أداة مدمجة في ويندوز لتنظيف الملفات المؤقتة والنظام. | مدمجة في Windows (ابحث عن "Disk Cleanup") |
| **TreeSize Free** | أداة لتحليل مساحة القرص وتحديد الملفات والمجلدات الكبيرة. | [تحميل TreeSize Free](https://www.jam-software.com/treesize_free) |
| **Autoruns** | أداة متقدمة من Microsoft Sysinternals لإدارة برامج بدء التشغيل والخدمات. | [تحميل Autoruns](https://docs.microsoft.com/en-us/sysinternals/downloads/autoruns) |
| **Dism++** | أداة متقدمة لإدارة صور Windows وتنظيف النظام. | [تحميل Dism++](https://github.com/Chuyu-Team/Dism-Multi-language/releases) |
| **PrivaZer** | أداة شاملة لتنظيف النظام وحماية الخصوصية وإزالة الآثار. | [تحميل PrivaZer](https://privazer.com/) |

---

### نصائح عامة:
- استخدم أدوات التنظيف بحذر وقم بعمل نسخة احتياطية قبل إجراء تغييرات كبيرة.
- تأكد من تحميل الأدوات من مصادرها الرسمية فقط.
- بعض الأدوات قد تحتاج صلاحيات مسؤول للعمل بكفاءة.
- راجع الإعدادات قبل تشغيل عمليات التنظيف لتجنب حذف ملفات مهمة.
