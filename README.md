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

| اسم الأداة | الوظيفة الأساسية | الرابط الرسمي |
|------------|-----------------|----------------|
| سيكلينر | تنظيف شامل للنظام وإزالة الملفات المؤقتة | [https://www.ccleaner.com](https://www.ccleaner.com) |
| مالوير بايتس أدابليان كلينر | إزالة البرامج الضارة والملفات الخبيثة | [https://www.malwarebytes.com/adwcleaner](https://www.malwarebytes.com/adwcleaner) |
| بليتشبيت كلينر | مسح آمن للبيانات الحساسة وحماية الخصوصية | [https://www.bleachbit.org](https://www.bleachbit.org) |
| آيو بت أدفانسد سيستم كير | صيانة شاملة للنظام وإصلاح السجل | [https://www.iobit.com/en/advancedcare.php](https://www.iobit.com/en/advancedcare.php) |
| جليري أوتيليتيز | تنظيف السجل وإدارة بدء التشغيل | [https://www.glarysoft.com](https://www.glarysoft.com) |
| أشامبو وين أوبتيمايزر | تحسين أداء ويندوز وتنظيف النظام | [https://www.ashampoo.com/en-usd/winoptimizer](https://www.ashampoo.com/en-usd/winoptimizer) |
| ديسك كلين آب | تنظيف القرص الصلب وإزالة الملفات غير المرغوبة | [https://www.kls-soft.com/dcu](https://www.kls-soft.com/dcu) |
| وايز كلينر | تنظيف سريع للنظام وحماية الخصوصية | [https://www.wisecleaner.com](https://www.wisecleaner.com) |
| برايفاسي إريسر | محو البيانات الشخصية بشكل آمن | [https://www.piriform.com/ccleaner/builds](https://www.piriform.com/ccleaner/builds) |
| سيستم نينجا | تنظيف وتحسين شامل للنظام | [https://singularlabs.com/software/system-ninja](https://singularlabs.com/software/system-ninja) |

---
## الرخصة
هذا المشروع مرخّص تحت رخصة MIT. راجع ملف LICENSE للمزيد.
