# Keylogger-Educational


## Lab Outline: Python Keylogger with Email Exfiltration

### Prerequisites
- Python installed
- Visual Studio Code
- Email Account

### Create Project Folder
<img width="885" alt="Screenshot 2025-03-21 at 9 42 05 AM" src="https://github.com/user-attachments/assets/3da03be1-399c-451b-9409-30972198ba0b" />



### Install Dependencies
<img width="885" alt="Screenshot 2025-03-21 at 9 43 28 AM" src="https://github.com/user-attachments/assets/f2d1ff14-c4d8-4f81-bc34-47ff3543475b" />




### Write Keylogger Script
<img width="885" alt="Screenshot 2025-03-21 at 9 43 28 AM" src="https://github.com/user-attachments/assets/7201508f-be10-476a-9b56-b828cce7967b" />



### Create a Gmail App Password
![Screenshot 2025-03-22 at 2 28 35 PM](https://github.com/user-attachments/assets/f21fed0b-6706-4ed0-9906-9bea82697399)



1. Go to https://myaccount.google.com/security
2. Enable 2-Step Verification
3. Click App Passwords
4. Create app name and generate password
5. Use that 16-character password in email_pass


### Make Configurations for Credentialed Scans (Within VM)
<img width="508" alt="image" src="https://github.com/joshmadakor1/openvas/assets/39254979/2ce2ea53-b67b-4206-8050-fecce0a11c52">

1. Disable Windows Firewall.
2. Disable User Account Control.
3. Enable Remote Registry.
4. Set Registry Key:
   - Launch Registry Editor (regedit.exe) in "Run as administrator" mode.
   - Navigate to HKEY_LOCAL_MACHINE hive.
   - Open SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System key.
   - Create a new DWORD (32-bit) value with the following properties:
     - Name: LocalAccountTokenFilterPolicy
     - Value: 1
   - Close Registry Editor.
5. Restart the VM.

### Make Configurations for Credentialed Scans (OpenVAS)
<img width="722" alt="image" src="https://github.com/joshmadakor1/openvas/assets/39254979/474cb714-19ad-4c99-8e60-945a2a12d7e5">

1. Go to Configuration > Credentials > New Credential.
2. Name / Comment: "Azure VM Credentials".
3. Allow Insecure Use: Yes.
4. Username: azureuser.
5. Password: Cyberlab123!
6. Save.
7. Go to Configuration > Targets > CLONE the Target we made before.
8. NEW Name / Comment: "Azure Vulnerable VMs - Credentialed Scan".
9. Ensure the Private IP is still accurate.
10. Credentials > SMB > Select the Credentials we just made: Azure VM Credentials.
11. Save.

### Execute Credentialed Scan against our Vulnerable Windows VM
<img width="1126" alt="image" src="https://github.com/joshmadakor1/openvas/assets/39254979/83467078-e917-4eba-9757-745fe47b4ebf">

<img width="861" alt="image" src="https://github.com/joshmadakor1/openvas/assets/39254979/3b5cf494-829c-4eb0-bcfd-6d4372c97cd6">

1. Within Greenbone / OpenVAS, go to Scans > Tasks.
2. CLONE the "Scan - Azure Vulnerable VMs" Task and Edit it.
3. Name / Comment: "Scan - Azure Vulnerable VMs - Credentialed".
4. Targets: Azure Vulnerable VMs - Credentialed Scan.
5. Save.
6. Click the Play button to launch the new Credentialed Scan and wait for it to finish.

### Remediate Vulnerabilities
<img width="799" alt="image" src="https://github.com/joshmadakor1/openvas/assets/39254979/6b3835dc-11b1-4e00-b7a5-baa8049182f7">

1. Log back into your Win10-Vulnerable VM.
2. Uninstall Adobe Reader, VLC Player, and Firefox.
3. Restart the VM.
4. Re-initiate the "Scan - Azure Vulnerable VMs - Credentialed" scan and observe the results.

### Verify Remediations
<img width="1120" alt="image" src="https://github.com/joshmadakor1/openvas/assets/39254979/9efbd193-002a-49c2-9d9e-51f2cf1dc2af">
