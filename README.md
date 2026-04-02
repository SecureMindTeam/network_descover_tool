# 🛡️ SecureMind Network Discover Tool

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Scapy-Security-red?style=for-the-badge" alt="Scapy">
  <img src="https://img.shields.io/badge/Blue_Team-SecureMind-blue?style=for-the-badge" alt="Blue Team">
</div>

## 📖 نبذة عن الأداة (Overview)
أداة **Network Discover Tool** هي أداة سريعة وفعالة تم تطويرها بواسطة فريق **SecureMind (Blue Team)**. تعتمد الأداة على بروتوكول **ARP (Address Resolution Protocol)** لاكتشاف الأجهزة الحية المتصلة بالشبكة المحلية (LAN). 

تعتبر هذه الأداة مفيدة جداً لمحللي مركز العمليات الأمنية (SOC) ومسؤولي الأنظمة لعمل حصر للأصول (Asset Discovery) واكتشاف أي أجهزة غير مصرح بها داخل الشبكة.

## ✨ المميزات (Features)
* إرسال حزم مسح (ARP Requests) لاكتشاف الأجهزة الحية.
* إظهار عنوان الـ IP وعنوان الـ MAC للأجهزة المكتشفة.
* واجهة سطر أوامر (CLI) منسقة واحترافية باستخدام مكتبتي `rich` و `pyfiglet`.
* خفيفة الوزن وسريعة التنفيذ.

## 🛠️ المتطلبات الأساسية (Prerequisites)
قبل تشغيل الأداة، تأكد من توفر الآتي:
* **Python 3.x** مثبت على نظامك.
* صلاحيات المسؤول (**Root/Administrator**) لأن مكتبة `scapy` تتطلب هذه الصلاحيات لإرسال حزم البيانات (Raw Packets) على مستوى الشبكة.

## ⚙️ التثبيت (Installation)

1. قم بعمل استنساخ (Clone) للمستودع:
   ```bash
   git clone [https://github.com/YourUsername/network-discover-tool.git](https://github.com/YourUsername/network-discover-tool.git)
   cd network-discover-tool
