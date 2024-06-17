import pickle
import os
from plyer import notification

# Caminho do arquivo de lembretes
FILE_PATH = "lembretes.pkl"

# Função para carregar lembretes
def load_reminders():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'rb') as file:
            return pickle.load(file)
    return []

# Função para salvar lembretes
def save_reminders(reminders):
    with open(FILE_PATH, 'wb') as file:
        pickle.dump(reminders, file)

# Função para adicionar lembrete
def add_reminder(reminders, reminder):
    reminders.append(reminder)
    save_reminders(reminders)
    notify("Lembrete Adicionado", reminder)
    print("Lembrete adicionado com sucesso!")

# Função para exibir lembretes
def view_reminders(reminders):
    if not reminders:
        print("Nenhum lembrete encontrado.")
    else:
        for index, reminder in enumerate(reminders, start=1):
            print(f"{index}. {reminder}")

# Função para excluir lembrete
def delete_reminder(reminders, index):
    if 0 <= index < len(reminders):
        removed = reminders.pop(index)
        save_reminders(reminders)
        notify("Lembrete Excluído", removed)
        print(f"Lembrete '{removed}' excluído com sucesso!")
    else:
        print("Índice inválido. Nenhum lembrete excluído.")

# Função para enviar notificação
def notify(title, message):
    try:
        notification.notify(
            title=title,
            message=message,
            app_name="Gerenciador de Lembretes",
            timeout=10  # duração da notificação em segundos
        )
    except Exception as e:
        print(f"Erro ao enviar notificação: {e}")

# Menu principal
def main():
    reminders = load_reminders()
    
    while True:
        print("\nGerenciador de Lembretes")
        print("1. Adicionar Lembrete")
        print("2. Visualizar Lembretes")
        print("3. Excluir Lembrete")
        print("4. Sair")
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            reminder = input("Digite o lembrete: ")
            add_reminder(reminders, reminder)
        elif choice == '2':
            view_reminders(reminders)
        elif choice == '3':
            view_reminders(reminders)
            try:
                index = int(input("Digite o índice do lembrete a excluir: ")) - 1
                delete_reminder(reminders, index)
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
        elif choice == '4':
            print("Saindo do gerenciador de lembretes.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
