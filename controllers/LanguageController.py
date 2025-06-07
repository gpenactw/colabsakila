class LanguageController:
    def __init__(self, model):
        self.model = model

    def list_languages(self):
        languages = self.model.get_all()
        print("\n--- Lista de Idiomas ---")
        for language in languages:
            print(f"{language.language_id}: {language.name}")

    def create_language(self):
        name = input("Nombre del idioma: ")
        
        if self.model.language_exists(name):
            print("Ya existe un idioma con ese nombre.")
            return
        
        try:
            self.model.add(name)
            print("Idioma creado exitosamente.")
        except Exception as err:
            print(f"Error al crear el idioma: {err}")

    def update_language(self):
        try:
            language_id = int(input("ID del idioma a actualizar: "))
        except ValueError:
            print("ID inválido.")
            return
        
        if not self.model.language_id_exists(language_id):
            print(f"No existe un idioma con ID {language_id}.")
            return
        
        name = input("Nuevo nombre del idioma: ")
        
        if self.model.language_exists(name, exclude_id=language_id):
            print("Ya existe un idioma con ese nombre.")
            return
        
        try:
            self.model.update(language_id, name)
            print("Idioma actualizado exitosamente.")
        except Exception as err:
            print(f"Error al actualizar el idioma: {err}")

    def delete_language(self):
        try:
            language_id = int(input("ID del idioma a eliminar: "))
        except ValueError:
            print("ID inválido. Debe ser un número entero.")
            return
        
        if not self.model.language_id_exists(language_id):
            print(f"No existe un idioma con ID {language_id}.")
            return
        
        confirm = input(f"¿Estás seguro de que deseas eliminar el idioma con ID {language_id}? (s/n): ").lower()
        if confirm != 's':
            print("Eliminación cancelada.")
            return
        
        try:
            self.model.delete(language_id)
            print("Idioma eliminado exitosamente.")
        except Exception as err:
            if hasattr(err, 'errno') and err.errno == 1451:
                print("No se puede eliminar el idioma: tiene películas asociadas.")
            else:
                print(f"Error al eliminar el idioma: {err}")