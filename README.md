# ERPNext Email Custom App

**⚠️ Warning:** Before installing this app, make sure ERPNext is installed on your system. This app depends on ERPNext and will not work standalone.

## Prerequisites
- Frappe Framework: v15.50.1 (version-15)
- ERPNext installed  v15.46.2 (version-15)

##Installation <br>
<b>Email Account should be configured, and a default sending option should also be set.</b>

cd ~/frappe-bench <br>
bench get-app item_notification https://github.com/shubhamg9074/Erpnext-Email.git <br>
bench --site your-site-name install-app item_notification <br>

<br>
<br>
<b>## Process</b>
<br>
Go to Item List and Create one Item <br>
Now Go to Sales Invoice List and Create Sales Invoice  With that Item <br><br><br>

Now Go to Item list and Click on Actions Button and Send Mail <br>
Check the Email in the Email Queue list.
