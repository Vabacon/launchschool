
passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']
password = ''
for _ in passcode:
    password += '{}-'.format(_) if _ != passcode[-1] else password + _
        
    

print(password)

# Expected output: 11-jZ5-hQ3f*-8!7g3-p3Fs