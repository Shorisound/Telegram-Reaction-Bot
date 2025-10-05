```markdown
# 🤖 Telegram Reaction Bot

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge&logo=python)
![Telegram](https://img.shields.io/badge/Telegram-Bot_API-blue?style=for-the-badge&logo=telegram)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 🌟 Descripción

Un script elegante y eficiente en Python que envía reacciones automáticas con emojis aleatorios a mensajes de Telegram utilizando múltiples bots simultáneamente.

---

## ✨ Características Principales

| Característica | Descripción |
|----------------|-------------|
| 🔥 **Múltiples Bots** | Soporte para varios tokens de bot simultáneos |
| 🎲 **Emojis Aleatorios** | Selección random de 11 emojis diferentes |
| ⚡ **Fácil Configuración** | Configuración simple mediante enlaces |
| 🚀 **Rápido y Eficiente** | Respuestas instantáneas usando la API oficial |

---

## 🛠️ Instalación Rápida

### Prerrequisitos
```bash
Python 3.6+ instalado
```

1. Clonar e Instalar

```bash
# Instalar dependencias
pip install requests

# Descargar el script
git clone https://github.com/Shorisound/Telegram-Reaction-Bot.git
cd telegram-reaction-bot
```

---

⚙️ Configuración

🔐 Obtención de Tokens

1. Ve a @BotFather en Telegram
2. Crea nuevos bots con /newbot
3. Copia los tokens generados

📝 Editar el Script

```python
bot_tokens = [
    "token_bot_1_123456:ABC_DEF",
    "token_bot_2_789012:GHI_JKL", 
    "token_bot_3_345678:MNO_PQR"
]

chat_id = "tu_chat_id_aqui"  # Ej: -1001234567890 o @nombre_grupo
```

---

🚀 Uso

Ejecución Simple

```bash
python telegram_reaction_bot.py
```

📥 Entrada de Datos

```
╔══════════════════════════════════════╗
║          LINK DEL MENSAJE           ║
╚══════════════════════════════════════╝

Link==> https://t.me/c/1234567890/123
```

📤 Salida Esperada

```
✅ Done √ ❤️‍🔥
✅ Done √ 🤯  
✅ Done √ 🥰
```

---

🎨 Emojis Disponibles

Emoji Descripción Frecuencia
❤️‍🔥 Corazón en llamas Aleatoria
🤯 Explosión mental Aleatoria
🥰 Cara sonriente con corazones Aleatoria
🔥 Fuego Aleatoria
😘 Cara enviando beso Aleatoria
🆒 Letra C cool Aleatoria
👍 Pulgar arriba Aleatoria
⚡ Rayo Aleatoria
👏 Aplausos Aleatoria
😍 Cara con ojos de corazón Aleatoria
🐳 Ballena Aleatoria

---

📋 Tabla de Comandos y Configuraciones

Parámetro Tipo Descripción Ejemplo
bot_tokens Lista Tokens de bots de Telegram ["token1", "token2"]
chat_id String ID del chat/grupo -1001234567890
message_id Int ID del mensaje (auto-extraído) 123
reaction Array Lista de reacciones a enviar [{"type": "emoji", "emoji": "🔥"}]

---

🐛 Solución de Problemas

❌ Error: "Chat not found"

```bash
✅ Solución: Verificar que el bot esté agregado al grupo
✅ Solución: Confirmar formato del chat_id
```

❌ Error: "Message not found"

```bash
✅ Solución: Revisar el enlace del mensaje
✅ Solución: Verificar permisos de lectura
```

❌ Error: "Bot is not a member"

```bash
✅ Solución: Agregar el bot al grupo manualmente
✅ Solución: Esperar a que se procese la invitación
```

---

📊 Estructura del Proyecto

```
telegram-reaction-bot/
├── 📄 telegram_reaction_bot.py
├── 📄 requirements.txt          
├── 📄 README.md               
```
---

🤝 Contribuciones

¡Las contribuciones son bienvenidas!

1. 🍴 Haz fork del proyecto
2. 🌿 Crea una rama para tu feature (git checkout -b feature/AmazingFeature)
3. 💬 Commit tus cambios (git commit -m 'Add AmazingFeature')
4. 🚀 Push a la rama (git push origin feature/AmazingFeature)
5. 🔄 Abre un Pull Request

---

📄 Licencia

Distribuido bajo la licencia MIT. Ver LICENSE para más información.

---

👨‍💻 Autor

Creado con ❤️ y ☕ por desarrolladores para la comunidad de Telegram.

---

<div align="center">

¿Te gusta este proyecto? ¡Dale una estrella! ⭐

</div>
```
