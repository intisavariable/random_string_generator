import secrets
import string
import pyautogui

def randomPassword():
    """Generate a random password """
    secrets_generator = secrets.SystemRandom()
    randomSource = string.ascii_letters + string.digits + string.punctuation
    password =  secrets_generator.choice(string.ascii_lowercase)
    password += secrets_generator.choice(string.ascii_uppercase)
    password += secrets_generator.choice(string.digits)
    password += secrets_generator.choice(string.punctuation)

    for _ in range(64):
        password += secrets_generator.choice(randomSource)

    passwordList = list(password)
    secrets_generator.shuffle(passwordList)
    password = ''.join(passwordList)
    return password
def randomScroll():
    secrets_generator = secrets.SystemRandom()
    ammount_to_scroll = secrets_generator.randrange(4096)
    pyautogui.scroll(ammount_to_scroll)
    

for _ in range (64*64):
    print (randomPassword()+'\n')
    
randomScroll()