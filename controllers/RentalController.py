from datetime import datetime

class RentalController:
    def __init__(self, model):
        self.model = model

    def list_rentals(self):
        rentals = self.model.get_all()
        print("\n--- Lista de Alquileres ---")
        if not rentals:
            print("No hay alquileres registrados.")
            return
        
        print(f"{'ID':>6} | {'Cliente':<25} | {'Película':<30} | {'Fecha Alquiler':<20} | {'Fecha Devolución':<20} | {'Staff':<25}")
        print("-" * 135)
        for rental in rentals:
            return_date = rental.return_date.strftime("%Y-%m-%d %H:%M:%S") if rental.return_date else "No devuelto"
            print(f"{rental.rental_id:>6} | {rental.customer_name:<25} | {rental.film_title:<30} | {rental.rental_date} | {return_date:<20} | {rental.staff_name:<25}")

    def create_rental(self):
        rental_date_input = input("Fecha de alquiler (YYYY-MM-DD HH:MM:SS) o Enter para fecha actual: ")
        if rental_date_input.strip():
            try:
                rental_date = datetime.strptime(rental_date_input, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                print("Formato de fecha inválido. Usando fecha actual.")
                rental_date = datetime.now()
        else:
            rental_date = datetime.now()

        try:
            inventory_id = int(input("ID del inventario: "))
            if not self.model.inventory_exists(inventory_id):
                print(f"Error: No existe un inventario con ID {inventory_id}.")
                return
            if not self.model.inventory_available(inventory_id):
                print(f"Error: El inventario {inventory_id} ya está alquilado.")
                return
        except ValueError:
            print("ID de inventario inválido.")
            return

        try:
            customer_id = int(input("ID del cliente: "))
            if not self.model.customer_exists(customer_id):
                print(f"Error: No existe un cliente con ID {customer_id}.")
                return
        except ValueError:
            print("ID de cliente inválido.")
            return

        try:
            staff_id = int(input("ID del personal: "))
            if not self.model.staff_exists(staff_id):
                print(f"Error: No existe un miembro del personal con ID {staff_id}.")
                return
        except ValueError:
            print("ID de personal inválido.")
            return

        try:
            self.model.add(rental_date, inventory_id, customer_id, staff_id)
            print("Alquiler registrado exitosamente.")
        except Exception as err:
            print(f"Error al registrar el alquiler: {err}")

    def update_rental(self):
        try:
            rental_id = int(input("ID del alquiler a actualizar: "))
        except ValueError:
            print("ID inválido.")
            return

        if not self.model.rental_id_exists(rental_id):
            print(f"No existe un alquiler con ID {rental_id}.")
            return

        rental = self.model.get_by_id(rental_id)
        print(f"\nAlquiler actual - Cliente: {rental.customer_id}, Inventario: {rental.inventory_id}, Fecha: {rental.rental_date}")

        rental_date_input = input(f"Nueva fecha de alquiler (actual: {rental.rental_date}, Enter para mantener): ")
        if rental_date_input.strip():
            try:
                rental_date = datetime.strptime(rental_date_input, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                print("Formato de fecha inválido. Manteniendo fecha actual.")
                rental_date = rental.rental_date
        else:
            rental_date = rental.rental_date

        try:
            inventory_id = int(input(f"Nuevo ID del inventario (actual: {rental.inventory_id}): "))
            if not self.model.inventory_exists(inventory_id):
                print(f"Error: No existe un inventario con ID {inventory_id}.")
                return
            if inventory_id != rental.inventory_id and not self.model.inventory_available(inventory_id):
                print(f"Error: El inventario {inventory_id} ya está alquilado.")
                return
        except ValueError:
            print("ID de inventario inválido.")
            return

        try:
            customer_id = int(input(f"Nuevo ID del cliente (actual: {rental.customer_id}): "))
            if not self.model.customer_exists(customer_id):
                print(f"Error: No existe un cliente con ID {customer_id}.")
                return
        except ValueError:
            print("ID de cliente inválido.")
            return

        return_date_str = rental.return_date.strftime("%Y-%m-%d %H:%M:%S") if rental.return_date else "N/A"
        return_date_input = input(f"Fecha de devolución (actual: {return_date_str}, Enter para mantener, 'clear' para eliminar): ")
        if return_date_input.strip().lower() == 'clear':
            return_date = None
        elif return_date_input.strip():
            try:
                return_date = datetime.strptime(return_date_input, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                print("Formato de fecha inválido. Manteniendo fecha actual.")
                return_date = rental.return_date
        else:
            return_date = rental.return_date

        try:
            staff_id = int(input(f"Nuevo ID del personal (actual: {rental.staff_id}): "))
            if not self.model.staff_exists(staff_id):
                print(f"Error: No existe un miembro del personal con ID {staff_id}.")
                return
        except ValueError:
            print("ID de personal inválido.")
            return

        try:
            self.model.update(rental_id, rental_date, inventory_id, customer_id, return_date, staff_id)
            print("Alquiler actualizado exitosamente.")
        except Exception as err:
            print(f"Error al actualizar el alquiler: {err}")

    def delete_rental(self):
        try:
            rental_id = int(input("ID del alquiler a eliminar: "))
        except ValueError:
            print("ID inválido. Debe ser un número entero.")
            return

        if not self.model.rental_id_exists(rental_id):
            print(f"No existe un alquiler con ID {rental_id}.")
            return

        rental = self.model.get_by_id(rental_id)
        print(f"\nAlquiler a eliminar - Cliente: {rental.customer_id}, Fecha: {rental.rental_date}")
        
        confirm = input(f"¿Estás seguro de que deseas eliminar el alquiler con ID {rental_id}? (s/n): ").lower()
        if confirm != 's':
            print("Eliminación cancelada.")
            return

        try:
            self.model.delete(rental_id)
            print("Alquiler eliminado exitosamente.")
        except Exception as err:
            if hasattr(err, 'errno') and err.errno == 1451:
                print("No se puede eliminar el alquiler: tiene pagos asociados.")
            else:
                print(f"Error al eliminar el alquiler: {err}")

    def show_active_rentals(self):
        rentals = self.model.get_active_rentals()
        print("\n--- Alquileres Activos (No Devueltos) ---")
        if not rentals:
            print("No hay alquileres activos.")
            return
        
        print(f"{'ID':>6} | {'Cliente':<25} | {'Película':<30} | {'Fecha Alquiler':<20}")
        print("-" * 85)
        for rental in rentals:
            days_rented = (datetime.now() - rental.rental_date).days
            print(f"{rental.rental_id:>6} | {rental.customer_name:<25} | {rental.film_title:<30} | {rental.rental_date} ({days_rented} días)")

    def return_rental(self):
        try:
            rental_id = int(input("ID del alquiler a devolver: "))
        except ValueError:
            print("ID inválido.")
            return

        if not self.model.rental_id_exists(rental_id):
            print(f"No existe un alquiler con ID {rental_id}.")
            return

        rental = self.model.get_by_id(rental_id)
        if rental.return_date:
            print(f"Este alquiler ya fue devuelto el {rental.return_date}.")
            return

        return_date_input = input("Fecha de devolución (YYYY-MM-DD HH:MM:SS) o Enter para fecha actual: ")
        if return_date_input.strip():
            try:
                return_date = datetime.strptime(return_date_input, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                print("Formato de fecha inválido. Usando fecha actual.")
                return_date = datetime.now()
        else:
            return_date = datetime.now()

        if return_date < rental.rental_date:
            print("Error: La fecha de devolución no puede ser anterior a la fecha de alquiler.")
            return

        try:
            self.model.return_rental(rental_id, return_date)
            print("Devolución registrada exitosamente.")
        except Exception as err:
            print(f"Error al registrar la devolución: {err}")