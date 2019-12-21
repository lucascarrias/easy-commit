import os
import subprocess

REPO = ''

def has_git():
    return os.path.isdir('.git')

def git_init():
    os.system('git init')
    return has_git()

def has_gitignore():
    return os.path.isfile('.gitignore')

def check_and_update_gitignore():
    if not has_gitignore():
            with open('.gitignore', 'w') as gi:
                gi.write(".gitignore\n{0}".format(__file__))
    else:
        with open('.gitignore', 'r') as gi:            
            for line in gi.readlines():                
                if __file__ == line.strip():                    
                    break
            else:
                with open('.gitignore', 'a') as gia:
                    gia.write("\n"+__file__)

def git_commit(msg):
    os.system("git add -A")
    msg = msg.strip().replace('"', '')
    os.system('git commit -m "%s"' % msg)

def check_remote_and_update():
    if system_output('git remote -v') == '':
        print('Repositório remoto não foi iniciado!\nPor favor adcionar link do repositório logo abaixo.')
        while True:
            REPO = input("Link do repositório>> ").strip()
            print("Verificando se o repositório já existe.")
            if 'fatal' not in system_output('git ls-remote ' + REPO):
                print('Repositório encontrado.')
                break
            else:
                print("Respositório não encontrado ou credenciais inválidas.\nPor favor repetir a operação.")
        os.system('git remote add %s %s' % (str(__file__)[:-3], REPO))

def git_push():
    os.system("git config credential.helper store 'cache --timeout=7200'")
    print(system_output('git push %s master' %  str(__file__)[:-3]))

def system_output(cmd):
    cmd = cmd.split()
    out = subprocess.Popen(cmd, 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)    
    return out.communicate()[0].decode('utf-8')

def main(): 
    if not has_git():
        print("Git não encontrado neste diretório.")
        print("Deseja inicializar o git neste diretório? (%s)" % (system_output('pwd').strip()))
        res = '#'
        while res[0].lower() not in 'ysn':
            res = input('(Yes or No)>>')
        if res[0].lower() in 'ys':            
            print("Git inicializado!" if git_init() else "Algum problema ocorreu ao tentar inicializar.")
        elif res[0].lower() in 'n':
            print("Por favor mover este script para o diretório desejado.")
    
    if has_git():
        check_and_update_gitignore()

        while True:
            action = input("1 - Commit\n2 - Push\n3 - Commit and Push\n4 - Sair\n>> ").strip()
            if action == '1':
                git_commit(input("Digite a mensagem do commit: "))
            elif action == '2':
                check_remote_and_update()              
                print("Tentando conectar ao repositório.")
                git_push()
            elif action == '3':
                git_commit(input("Digite a mensagem do commit: "))
                check_remote_and_update()              
                print("Tentando conectar ao repositório.")
                git_push()
            elif action == '4':
                break
                

if __name__ == "__main__":
    main()