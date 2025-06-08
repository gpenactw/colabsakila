class FilmController:
    def __init__(self, model):
        self.model = model

    def list_films(self):
        films = self.model.get_all()
        print("\n--- Lista de Películas ---")
        for film in films:
            print(
                f"ID: {film.film_id}, Título: {film.title}, Descripción: {film.description}, Año de lanzamiento: {film.release_year}, "
                f"ID de idioma: {film.language_id}, ID de idioma original: {film.original_language_id}, "
                f"Duración del alquiler: {film.rental_duration} días, Tarifa de alquiler: {film.rental_rate}, "
                f"Duración: {film.length} minutos, Costo de reemplazo: {film.replacement_cost}, "
                f"Clasificación: {film.rating}, Características especiales: {film.special_features}, "
                f"Última actualización: {film.last_update}")

    def create_film(self):
        title = input("Título: ")
        description = input("Descripción: ")
        release_year_input = input("Año de lanzamiento: ")
        try:
            release_year = int(release_year_input)
        except ValueError:
            print("Año de lanzamiento inválido. Se usará 2000 por defecto.")
            release_year = 2000
        
        try:
            language_id = int(input("ID de idioma: "))
        except ValueError:
            print("ID de idioma inválido.")
            return
        original_language_id_input = input("ID de idioma original (opcional): ")
        original_language_id = int(original_language_id_input) if original_language_id_input.strip() else None
        rental_input = input("Duración del alquiler (en días): ")
        try:
            rental_duration = int(rental_input)
            if rental_duration <= 0:
                print("Duración del alquiler no válida. Se establecerá en 3 días.")
                rental_duration = 3
        except ValueError:
            print("Duración del alquiler no válida. Se establecerá en 3 días.")
            rental_duration = 3
        rental_rate_input = input("Tarifa de alquiler (0.00 - 99.99): ")
        try:
            rental_rate = float(rental_rate_input)
            if rental_rate < 0 or rental_rate > 99.99:
                print("Tarifa fuera de rango. Se establecerá en 4.99.")
                rental_rate = 4.99
        except ValueError:
            print("Tarifa inválida. Se establecerá en 4.99.")
            rental_rate = 4.99
        length_input = input("Duración (en minutos): ")
        try:
            length = int(length_input)
        except ValueError:
            length = None
        replacement_cost_input = input("Costo de reemplazo (0.00 - 999.99): ")
        try:
            replacement_cost = float(replacement_cost_input)
            if replacement_cost < 0 or replacement_cost > 999.99:
                print("Costo fuera de rango. Se establecerá en 19.99.")
                replacement_cost = 19.99
        except ValueError:
            print("Costo de reemplazo no válido. Se establecerá en 19.99.")
            replacement_cost = 19.99

        rating = input("Clasificación (G, PG, PG-13, R, NC-17): ").upper()
        valid_ratings = ['G', 'PG', 'PG-13', 'R', 'NC-17']
        if rating not in valid_ratings:
            print(f"Clasificación inválida. Debe ser una de: {', '.join(valid_ratings)}. Se usará 'G' por defecto.")
            rating = 'G'
        
        special_features = input("Características especiales (separadas por comas): ")

        if self.model.film_exists(title, release_year):
            print("Ya existe una película con ese título y año.")
            return

        try:
            print(f"\n[DEBUG] Creando película con los siguientes datos:")
            print(f"  Título: {title}")
            print(f"  Año: {release_year}")
            print(f"  ID Idioma: {language_id}")
            print(f"  ID Idioma Original: {original_language_id}")
            print(f"  Duración alquiler: {rental_duration}")
            print(f"  Tarifa: {rental_rate}")
            print(f"  Duración: {length}")
            print(f"  Costo reemplazo: {replacement_cost}")
            print(f"  Rating: {rating}")
            print(f"  Características: {special_features}")
            
            self.model.add(title, description, release_year, language_id, original_language_id, rental_duration,
                           rental_rate, length, replacement_cost, rating, special_features)
            print("\n Película creada exitosamente.")
        except Exception as err:
            print(f"\n Error al crear película:")
            print(f"   Tipo de error: {type(err).__name__}")
            print(f"   Mensaje: {str(err)}")
            
            if hasattr(err, 'errno'):
                if err.errno == 1452:
                    print("\n   Causa: El ID de idioma especificado no existe en la tabla language.")
                    print("   Solución: Use un ID de idioma válido (generalmente 1 para English).")
                elif err.errno == 1406:
                    print("\n   Causa: Uno de los valores es demasiado largo para el campo.")
                elif err.errno == 1062:
                    print("\n   Causa: Violación de clave única.")
                elif err.errno == 1264:
                    print("\n   Causa: Valor fuera de rango para un campo numérico.")
                    print("   Solución: Verifique que rental_rate esté entre 0.00 y 99.99")
                    print("            y que replacement_cost esté entre 0.00 y 999.99")
            else:
                print(f"\n   Error completo: {err}")

    def update_film(self):
        try:
            film_id = int(input("ID de la película a actualizar: "))
        except ValueError:
            print("ID inválido.")
            return

        if not self.model.film_id_exists(film_id):  # Este método lo debes tener en tu modelo
            print(f"No existe una película con ID {film_id}.")
            return

        title = input("Título actualizado: ")
        description = input("Actualización descripción: ")

        release_year_input = input("Actualización año de lanzamiento: ")
        try:
            release_year = int(release_year_input)
        except ValueError:
            print("Año inválido. Se usará 2000 por defecto.")
            release_year = 2000

        try:
            language_id = int(input("Actualización ID de idioma: "))
        except ValueError:
            print("ID de idioma inválido.")
            return

        original_language_id_input = input("ID de idioma original (opcional) actualizado: ")
        original_language_id = int(original_language_id_input) if original_language_id_input.strip() else None

        rental_input = input("Actualización duración del alquiler (en días): ")
        try:
            rental_duration = int(rental_input)
            if rental_duration <= 0:
                print("Duración inválida. Se establecerá en 3 días.")
                rental_duration = 3
        except ValueError:
            print("Duración inválida. Se establecerá en 3 días.")
            rental_duration = 3

        rental_rate_input = input("Actualización tarifa de alquiler (0.00 - 99.99): ")
        try:
            rental_rate = float(rental_rate_input)
            if rental_rate < 0 or rental_rate > 99.99:
                print("Tarifa fuera de rango. Se establecerá en 4.99.")
                rental_rate = 4.99
        except ValueError:
            print("Tarifa inválida. Se establecerá en 4.99.")
            rental_rate = 4.99

        length_input = input("Actualización duración (en minutos): ")
        try:
            length = int(length_input)
        except ValueError:
            length = None

        replacement_cost_input = input("Actualización costo de reemplazo (0.00 - 999.99): ")
        try:
            replacement_cost = float(replacement_cost_input)
            if replacement_cost < 0 or replacement_cost > 999.99:
                print("Costo fuera de rango. Se establecerá en 19.99.")
                replacement_cost = 19.99
        except ValueError:
            print("Costo inválido. Se establecerá en 19.99.")
            replacement_cost = 19.99

        rating = input("Actualización clasificación: ").upper()
        valid_ratings = ['G', 'PG', 'PG-13', 'R', 'NC-17']
        if rating not in valid_ratings:
            print("Clasificación inválida. Se establecerá en 'G'.")
            rating = 'G'

        special_features = input("Actualización características especiales: ")

        # Verificar si ya existe otra película con el mismo título y año (evita duplicados)
        if self.model.film_exists(title, release_year, exclude_id=film_id):
            print("Ya existe una película con ese título y año.")
            return

        try:
            self.model.update(
                film_id, title, description, release_year, language_id,
                original_language_id, rental_duration, rental_rate, length,
                replacement_cost, rating, special_features
            )
            print("Película actualizada exitosamente.")
        except Exception as err:
            if hasattr(err, 'errno') and err.errno == 1452:
                print("Error: El ID de idioma no existe en la tabla language.")
            else:
                print(f"Error inesperado al actualizar Película: {err}")

    def delete_film(self):
        try:
            film_id = int(input("ID de la película a eliminar: "))
        except ValueError:
            print("ID inválido. Debe ser un número entero.")
            return

        if not self.model.film_id_exists(film_id):
            print(f"No existe una película con ID {film_id}.")
            return

        # Verificar registros relacionados
        actors_count = self.model.get_related_actors_count(film_id)
        categories_count = self.model.get_related_categories_count(film_id)
        inventory_count = self.model.get_related_inventory_count(film_id)
        
        if actors_count > 0 or categories_count > 0 or inventory_count > 0:
            print(f"\nLa película con ID {film_id} tiene registros relacionados:")
            if actors_count > 0:
                print(f"   - {actors_count} actores asociados")
            if categories_count > 0:
                print(f"   - {categories_count} categorías asociadas")
            if inventory_count > 0:
                print(f"   - {inventory_count} items en inventario")
            print("\nPara eliminar esta película, primero debe eliminar estos registros relacionados.")
            return

        confirm = input(f"¿Estás seguro de que deseas eliminar la película con ID {film_id}? (s/n): ").lower()
        if confirm != 's':
            print("Eliminación cancelada.")
            return

        try:
            self.model.delete(film_id)
            print("Película eliminada exitosamente.")
        except Exception as err:
            if hasattr(err, 'errno') and err.errno == 1451:
                print(
                    "No se puede eliminar la película: tiene registros relacionados (por ejemplo, en inventory o rental).")
            else:
                print(f"Error inesperado al eliminar película: {err}")