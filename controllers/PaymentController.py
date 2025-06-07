from datetime import datetime

class PaymentController:
    def __init__(self, model):
        self.model = model

    def list_payments(self):
        payments = self.model.get_all()
        print("\n--- Lista de Pagos ---")
        if not payments:
            print("No hay pagos registrados.")
            return
        
        print(f"{'ID':>8} | {'Cliente':<25} | {'Staff':<25} | {'Alquiler':>8} | {'Monto':>10} | {'Fecha':<20}")
        print("-" * 110)
        for payment in payments:
            customer_name = getattr(payment, 'customer_name', f"ID: {payment.customer_id}")
            staff_name = getattr(payment, 'staff_name', f"ID: {payment.staff_id}")
            rental_id = payment.rental_id if payment.rental_id else "N/A"
            print(f"{payment.payment_id:>8} | {customer_name:<25} | {staff_name:<25} | {rental_id:>8} | ${payment.amount:>9.2f} | {payment.payment_date}")

    def create_payment(self):
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

        rental_id_input = input("ID del alquiler (opcional, presiona Enter para omitir): ")
        rental_id = None
        if rental_id_input.strip():
            try:
                rental_id = int(rental_id_input)
                if not self.model.rental_exists(rental_id):
                    print(f"Error: No existe un alquiler con ID {rental_id}.")
                    return
            except ValueError:
                print("ID de alquiler inválido.")
                return

        try:
            amount = float(input("Monto del pago: $"))
            if amount <= 0:
                print("El monto debe ser mayor que cero.")
                return
        except ValueError:
            print("Monto inválido.")
            return

        payment_date_input = input("Fecha del pago (YYYY-MM-DD HH:MM:SS) o Enter para fecha actual: ")
        if payment_date_input.strip():
            try:
                payment_date = datetime.strptime(payment_date_input, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                print("Formato de fecha inválido. Usando fecha actual.")
                payment_date = datetime.now()
        else:
            payment_date = datetime.now()

        try:
            self.model.add(customer_id, staff_id, rental_id, amount, payment_date)
            print("Pago registrado exitosamente.")
        except Exception as err:
            print(f"Error al registrar el pago: {err}")

    def update_payment(self):
        try:
            payment_id = int(input("ID del pago a actualizar: "))
        except ValueError:
            print("ID inválido.")
            return

        if not self.model.payment_id_exists(payment_id):
            print(f"No existe un pago con ID {payment_id}.")
            return

        payment = self.model.get_by_id(payment_id)
        print(f"\nPago actual - Cliente: {payment.customer_id}, Staff: {payment.staff_id}, Monto: ${payment.amount}")

        try:
            customer_id = int(input(f"Nuevo ID del cliente (actual: {payment.customer_id}): "))
            if not self.model.customer_exists(customer_id):
                print(f"Error: No existe un cliente con ID {customer_id}.")
                return
        except ValueError:
            print("ID de cliente inválido.")
            return

        try:
            staff_id = int(input(f"Nuevo ID del personal (actual: {payment.staff_id}): "))
            if not self.model.staff_exists(staff_id):
                print(f"Error: No existe un miembro del personal con ID {staff_id}.")
                return
        except ValueError:
            print("ID de personal inválido.")
            return

        current_rental = payment.rental_id if payment.rental_id else "N/A"
        rental_id_input = input(f"Nuevo ID del alquiler (actual: {current_rental}, Enter para omitir): ")
        rental_id = None
        if rental_id_input.strip():
            try:
                rental_id = int(rental_id_input)
                if not self.model.rental_exists(rental_id):
                    print(f"Error: No existe un alquiler con ID {rental_id}.")
                    return
            except ValueError:
                print("ID de alquiler inválido.")
                return

        try:
            amount = float(input(f"Nuevo monto (actual: ${payment.amount}): $"))
            if amount <= 0:
                print("El monto debe ser mayor que cero.")
                return
        except ValueError:
            print("Monto inválido.")
            return

        payment_date_input = input(f"Nueva fecha (actual: {payment.payment_date}, Enter para mantener): ")
        if payment_date_input.strip():
            try:
                payment_date = datetime.strptime(payment_date_input, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                print("Formato de fecha inválido. Manteniendo fecha actual.")
                payment_date = payment.payment_date
        else:
            payment_date = payment.payment_date

        try:
            self.model.update(payment_id, customer_id, staff_id, rental_id, amount, payment_date)
            print("Pago actualizado exitosamente.")
        except Exception as err:
            print(f"Error al actualizar el pago: {err}")

    def delete_payment(self):
        try:
            payment_id = int(input("ID del pago a eliminar: "))
        except ValueError:
            print("ID inválido. Debe ser un número entero.")
            return

        if not self.model.payment_id_exists(payment_id):
            print(f"No existe un pago con ID {payment_id}.")
            return

        payment = self.model.get_by_id(payment_id)
        print(f"\nPago a eliminar - Monto: ${payment.amount}, Fecha: {payment.payment_date}")
        
        confirm = input(f"¿Estás seguro de que deseas eliminar el pago con ID {payment_id}? (s/n): ").lower()
        if confirm != 's':
            print("Eliminación cancelada.")
            return

        try:
            self.model.delete(payment_id)
            print("Pago eliminado exitosamente.")
        except Exception as err:
            print(f"Error al eliminar el pago: {err}")

    def show_customer_total(self):
        try:
            customer_id = int(input("ID del cliente: "))
            if not self.model.customer_exists(customer_id):
                print(f"No existe un cliente con ID {customer_id}.")
                return
        except ValueError:
            print("ID de cliente inválido.")
            return

        total = self.model.get_total_by_customer(customer_id)
        print(f"\nTotal de pagos del cliente {customer_id}: ${total:.2f}")

    def show_payments_by_date(self):
        start_date_input = input("Fecha inicial (YYYY-MM-DD): ")
        try:
            start_date = datetime.strptime(start_date_input, "%Y-%m-%d")
        except ValueError:
            print("Formato de fecha inicial inválido.")
            return

        end_date_input = input("Fecha final (YYYY-MM-DD): ")
        try:
            end_date = datetime.strptime(end_date_input + " 23:59:59", "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("Formato de fecha final inválido.")
            return

        payments = self.model.get_payments_by_date_range(start_date, end_date)
        if not payments:
            print(f"\nNo hay pagos entre {start_date_input} y {end_date_input}.")
            return

        print(f"\n--- Pagos entre {start_date_input} y {end_date_input} ---")
        total = 0
        for payment in payments:
            print(f"ID: {payment.payment_id}, Cliente: {payment.customer_id}, Monto: ${payment.amount:.2f}, Fecha: {payment.payment_date}")
            total += payment.amount
        print(f"\nTotal: ${total:.2f}")