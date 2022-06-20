import tensorflow as tf
import tensorflow_text as text

model = tf.keras.models.load_model('SMSSpamModel')
y = model.predict([
    "http://paperok.ml - Professional academic help for you!",
    "You know what the warmer weather means...it's burn season! 🔥 Just ask me to roast one of ur friends. I'll take care of the rest 😎",
    "Hi Jiatang, this is Niall from Integrity Power Search, a boutique recruiting firm that works with high-growth tech companies on full-time opportunities. I recently sent you an email regarding a 100% Remote Senior - Principal Engineer @ The Largest SaaS Recruiting Company. Are you open to hearing more about our client and this role? Feel free to connect with me here: https://www.linkedin.com/in/niall-clancey-757847120/ Reply stop to unsubscribe.",
    "Your package is waiting for delivery. Please confirm the settlement of $19.99 on the following link: http://aka.ms/adfuyiwy",
    "NHS: we have identified that you are eligible to apply for your vaccine. For more information and apply, follow here: application-ukform.com",
    "Hi, Darya. When I test the iOS telemetry today, I found the same issue with \"New Chat Open\" event. I've ready report a bug for that."
])
print(y)