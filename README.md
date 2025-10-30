# منظف النظام الذكي (Smart System Cleaner)
- يمكنك استثناء أي مسار أو نوع ملف قبل التنفيذ.
4) التنفيذ والتراجع
- بعد التأكيد، ينفذ الأداة الحذف الآمن.
- ينشئ نقطة استعادة بسيطة (اختيارية) أو سلة مهملات داخلية لاسترجاع الملفات خلال جلسة واحدة.
---
## أنواع الملفات المستهدفة (قابلة للتخصيص)
- ملفات الكاش المؤقتة: tmp, cache, .DS_Store, Thumbs.db
- سجلات قديمة ومتضخمة: .log (مع حد زمني افتراضي > 30 يوم)
- ملفات التحديثات المؤقتة وحِزم التنزيل غير المكتملة
- مخلفات حزم مديري الحزم (npm, pip, pipenv, yarn) ضمن مجلدات العمل القديمة
- ذاكرة المتصفحات المؤقتة (عند توفر صلاحيات المستخدم)
تحذير لطيف: لن يُحذف أي شيء حساس بدون موافقتك الصريحة.
---
## تشغيل المشروع محلياً
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
  - --mode [fast|deep|custom]
  - --dry-run لمعاينة النتائج دون حذف
  - --paths لتحديد مجلدات إضافية
  - --exclude لاستثناء أنماط معيّنة
---
## بنية المشروع
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
## خارطة الطريق (Roadmap)
- إضافة واجهة رسومية فعلية ببايثون (PySide6/Qt) أو Electron.
- تكامل مع مكتبات الرسم البياني (matplotlib/plotly أو chart.js) لعرض النتائج.
- وحدة ذكاء بسيطة لتعلّم أنماط الاستخدام واقتراح تنظيفات مستقبلية.
- دعم جدولة التنظيف التلقائي وإشعارات قبل/بعد التنفيذ.
---
## أدوات بديلة مشهورة لتنظيف وتحسين النظام:

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
| System Ninja | تنظيف الجهاز وإزالة الملفات الغير ضرورية وتحسين الأداء | [https://singularlabs.com/software/system-ninja/](https://singularlabs.com/software/system-ninja/) |
