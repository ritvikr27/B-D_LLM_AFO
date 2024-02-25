css= '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #03dbfc
}
.chat-message.bot {
    background-color: #243c40
}
.chat-message .avatar {
  width: 15%;
}
.chat-message .avatar img {
  max-width: 72px;
  max-height: 60px;
  border-radius: 25%;
  object-fit: cover;
}
.chat-message .message {
  width: 90%;
  padding: 0 3.5rem;
  color: #615b36;
}
'''

bot_template= '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.pinimg.com/originals/c5/85/02/c585020c352da39533529eb6a6feb6c0.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template= '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://64.media.tumblr.com/009e6301398168ccc1ffa13ff17a8f72/0f2b2428db1e013b-9d/s1280x1920/85989500a9a2321f4e1e1010cdfb9a63e0aa057b.jpg">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
