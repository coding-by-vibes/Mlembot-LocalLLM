# 🛠️ Discord Developer Portal Setup

This guide walks you through setting up the Discord Developer side of Mlembot so it can be self-hosted on another machine.

---

## ✅ Step 1: Go to the Discord Developer Portal

Visit [https://discord.com/developers/applications](https://discord.com/developers/applications)

---

## ✅ Step 2: Create a New Application

- Click **“New Application”**
- Name it something like `Mlembot`
- Click **“Create”**

---

## ✅ Step 3: Configure the Bot

1. Click the **Bot** tab on the left.
2. Click **“Add Bot”** and confirm.
3. Enable the following under **Privileged Gateway Intents**:
   - ✅ `MESSAGE CONTENT INTENT`
   - ✅ `SERVER MEMBERS INTENT` *(optional for name lookup)*

---

## ✅ Step 4: Copy the Bot Token

- Still in the **Bot** tab, click **“Reset Token”** if needed.
- Click **“Copy”**
- Paste it into your `.env` file like this:

```env
DISCORD_BOT_TOKEN=your_token_here
```

---

## ✅ Step 5: OAuth2 Settings and Invite URL

1. Go to **OAuth2 → URL Generator**
2. Under **Scopes**, check:
   - ✅ `bot`
   - ✅ `applications.commands`
3. Under **Bot Permissions**, check:
   - ✅ `Send Messages`
   - ✅ `Read Message History`
   - ✅ `Use Application Commands`
   - *(Optional: `Embed Links`, `Attach Files`, `Manage Messages` if needed)*

4. Copy the **generated invite URL** to invite your bot to any server.

---

## 🧪 Example Invite URL Format

```
https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&scope=bot+applications.commands&permissions=277025508352
```

Replace `YOUR_CLIENT_ID` with your bot's Application ID (found in the **General Information** tab).

---

That's it! Your bot is ready to run on any machine with the proper `.env` and environment.
