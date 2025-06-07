class StaffController:
    def __init__(self, model):
        self.model = model

    def list_staff(self):
        staff_list = self.model.get_all()
        print("\n--- Lista de Personal ---")
        if not staff_list:
            print("No hay personal registrado.")
            return
        
        print(f"{'ID':>4} | {'Nombre':<25} | {'Usuario':<15} | {'Email':<30} | {'Tienda':>6} | {'Activo':<6} | {'Dirección':<40}")
        print("-" * 145)
        for staff in staff_list:
            active_status = "Sí" if staff.active else "No"
            address = getattr(staff, 'full_address', f"ID: {staff.address_id}")
            print(f"{staff.staff_id:>4} | {staff.first_name} {staff.last_name:<20} | {staff.username:<15} | {staff.email or 'N/A':<30} | {staff.store_id:>6} | {active_status:<6} | {address[:40]:<40}")

    def create_staff(self):
        first_name = input("Nombre: ")
        last_name = input("Apellido: ")
        
        try:
            address_id = int(input("ID de dirección: "))
            if not self.model.address_exists(address_id):
                print(f"Error: No existe una dirección con ID {address_id}.")
                return
        except ValueError:
            print("ID de dirección inválido.")
            return

        email = input("Email (opcional): ").strip() or None
        if email and self.model.email_exists(email):
            print("Ya existe un miembro del personal con ese email.")
            return

        try:
            store_id = int(input("ID de tienda: "))
            if not self.model.store_exists(store_id):
                print(f"Error: No existe una tienda con ID {store_id}.")
                return
        except ValueError:
            print("ID de tienda inválido.")
            return

        active_input = input("¿Activo? (s/n): ").lower()
        active = 1 if active_input == 's' else 0

        username = input("Nombre de usuario: ")
        if self.model.username_exists(username):
            print("Ya existe un miembro del personal con ese nombre de usuario.")
            return

        password = input("Contraseña: ")

        try:
            self.model.add(first_name, last_name, address_id, email, store_id, active, username, password)
            print("Personal creado exitosamente.")
        except Exception as err:
            print(f"Error al crear el personal: {err}")

    def update_staff(self):
        try:
            staff_id = int(input("ID del personal a actualizar: "))
        except ValueError:
            print("ID inválido.")
            return

        if not self.model.staff_id_exists(staff_id):
            print(f"No existe personal con ID {staff_id}.")
            return

        staff = self.model.get_by_id(staff_id)
        print(f"\nPersonal actual: {staff.first_name} {staff.last_name} - Usuario: {staff.username}")

        first_name = input(f"Nuevo nombre (actual: {staff.first_name}): ") or staff.first_name
        last_name = input(f"Nuevo apellido (actual: {staff.last_name}): ") or staff.last_name

        try:
            address_input = input(f"Nuevo ID de dirección (actual: {staff.address_id}): ")
            address_id = int(address_input) if address_input else staff.address_id
            if address_id != staff.address_id and not self.model.address_exists(address_id):
                print(f"Error: No existe una dirección con ID {address_id}.")
                return
        except ValueError:
            print("ID de dirección inválido.")
            return

        email_input = input(f"Nuevo email (actual: {staff.email or 'N/A'}): ").strip()
        email = email_input if email_input else staff.email
        if email and email != staff.email and self.model.email_exists(email, exclude_id=staff_id):
            print("Ya existe un miembro del personal con ese email.")
            return

        try:
            store_input = input(f"Nuevo ID de tienda (actual: {staff.store_id}): ")
            store_id = int(store_input) if store_input else staff.store_id
            if store_id != staff.store_id and not self.model.store_exists(store_id):
                print(f"Error: No existe una tienda con ID {store_id}.")
                return
        except ValueError:
            print("ID de tienda inválido.")
            return

        active_status = "Sí" if staff.active else "No"
        active_input = input(f"¿Activo? (actual: {active_status}, s/n): ").lower()
        if active_input:
            active = 1 if active_input == 's' else 0
        else:
            active = staff.active

        username = input(f"Nuevo nombre de usuario (actual: {staff.username}): ") or staff.username
        if username != staff.username and self.model.username_exists(username, exclude_id=staff_id):
            print("Ya existe un miembro del personal con ese nombre de usuario.")
            return

        change_password = input("¿Cambiar contraseña? (s/n): ").lower()
        password = None
        if change_password == 's':
            password = input("Nueva contraseña: ")

        try:
            self.model.update(staff_id, first_name, last_name, address_id, email, store_id, active, username, password)
            print("Personal actualizado exitosamente.")
        except Exception as err:
            print(f"Error al actualizar el personal: {err}")

    def delete_staff(self):
        try:
            staff_id = int(input("ID del personal a eliminar: "))
        except ValueError:
            print("ID inválido. Debe ser un número entero.")
            return

        if not self.model.staff_id_exists(staff_id):
            print(f"No existe personal con ID {staff_id}.")
            return

        staff = self.model.get_by_id(staff_id)
        print(f"\nPersonal a eliminar: {staff.first_name} {staff.last_name} - Usuario: {staff.username}")
        
        confirm = input(f"¿Estás seguro de que deseas eliminar al personal con ID {staff_id}? (s/n): ").lower()
        if confirm != 's':
            print("Eliminación cancelada.")
            return

        try:
            self.model.delete(staff_id)
            print("Personal eliminado exitosamente.")
        except Exception as err:
            if hasattr(err, 'errno') and err.errno == 1451:
                print("No se puede eliminar el personal: tiene registros relacionados (alquileres, pagos, o es gerente de tienda).")
            else:
                print(f"Error al eliminar el personal: {err}")

    def show_active_staff(self):
        staff_list = self.model.get_active_staff()
        print("\n--- Personal Activo ---")
        if not staff_list:
            print("No hay personal activo.")
            return
        
        print(f"{'ID':>4} | {'Nombre':<25} | {'Usuario':<15} | {'Email':<30} | {'Tienda':>6}")
        print("-" * 90)
        for staff in staff_list:
            print(f"{staff.staff_id:>4} | {staff.first_name} {staff.last_name:<20} | {staff.username:<15} | {staff.email or 'N/A':<30} | {staff.store_id:>6}")