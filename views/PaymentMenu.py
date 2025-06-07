class PaymentMenu:
    def __init__(self, controller, db):
        self.controller = controller
        self.db = db

    def display(self):
        while True:
            print("\n=== MENÚ DE PAGOS ===")
            print("1. Listar todos los pagos")
            print("2. Registrar nuevo pago")
            print("3. Actualizar pago")
            print("4. Eliminar pago")
            print("5. Ver total de pagos por cliente")
            print("6. Ver pagos por rango de fechas")
            print("7. Volver al menú principal")
            
            choice = input("Selecciona una opción: ")

            if choice == "1":
                self.controller.list_payments()
            elif choice == "2":
                self.controller.create_payment()
            elif choice == "3":
                self.controller.update_payment()
            elif choice == "4":
                self.controller.delete_payment()
            elif choice == "5":
                self.controller.show_customer_total()
            elif choice == "6":
                self.controller.show_payments_by_date()
            elif choice == "7":
                print("Volviendo al menú principal...")
                break
            else:
                print("Opción inválida.")