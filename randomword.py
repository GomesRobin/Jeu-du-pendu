import random

def load_words_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            words = [line.strip() for line in file.readlines() if line.strip()]  # Lire les mots du fichier
        return words
    except FileNotFoundError:
        print(f"Le fichier '{file_name}' n'a pas été trouvé.")
        return []
    except Exception as e:
        print(f"Une erreur s'est produite lors de la lecture du fichier : {e}")
        return []
    
def display(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def load_best_score(file_name):
    try:
        with open(file_name, 'r') as file:
            best_score = int(file.read().strip())
        return best_score
    except FileNotFoundError:
        return float('inf')  # Meilleur score initialisé à l'infini (aucun score existant)
    except Exception as e:
        print(f"Une erreur s'est produite lors de la lecture du meilleur score : {e}")
        return float('inf')
    
def save_best_score(file_name, best_score):
    try:
        with open(file_name, 'w') as file:
            file.write(str(best_score))
    except Exception as e:
        print(f"Une erreur s'est produite lors de la sauvegarde du meilleur score : {e}")



def main(file_name, best_score_file):
    words = load_words_from_file(file_name)
    
    if not words:
        print("Aucun mot valide n'a été chargé. Le jeu ne peut pas continuer.")
        return

    choise_word = random.choice(words)

    tentative_max = 10
    tentative = 0

    lettre_correct = []
    best_score = load_best_score(best_score_file)

    while tentative < tentative_max:
        current_display = display(choise_word, lettre_correct)
        print(f"Mot actuel : {current_display}")
        
        letter = input("Donnez-moi une lettre : ")

        if len(letter) != 1 or not letter.isalpha():
            print("Veuillez entrer une lettre valide !")
            continue
        if letter in lettre_correct:
            print("Vous avez déjà deviné cette lettre.")
            continue
        if letter in choise_word:
            print("Vous avez trouvé une lettre du mot !")
            lettre_correct.append(letter)
        else:
            print("La lettre n'est pas dans le mot.")
            tentative += 1

        if set(lettre_correct) == set(choise_word):
            print(f"Vous avez trouvé le mot, '{choise_word}' !")

            if tentative < best_score:
                print(f"Meilleur score de tous les temps !!! Vous avez battu le record !")
                save_best_score(best_score_file, tentative)
            else:
                print(f"Vous avez battu le mot, '{choise_word}' en {tentative} tentatives. Le record est de {best_score} tentatives.")
            
            break

    else:
        print(f"Désolé, vous avez utilisé toutes vos tentatives. Le mot était '{choise_word}'.")



if __name__ == "__main__":
    file_name = "liste_de_mots.txt"  # Remplacez le nom de fichier par "liste_de_mots.txt"
    best_score_file = "best_scores.txt"  # Fichier pour stocker le meilleur score
    main(file_name, best_score_file)
