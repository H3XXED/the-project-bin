import xml.etree.ElementTree as ET


def parse_orders(root):
    """
    Parses the XML root element and returns a list of dictionaries, where each dictionary represents an order.

    Parameters:
    root (Element): The root element of the XML file.

    Returns:
    A list of dictionaries, where each dictionary represents an order. Each dictionary contains the following keys:
    - 'id' (string): The ID of the order.
    - 'warehouse' (string): The warehouse that the order is coming from.
    - 'shipped' (string): A string representing whether the order has been shipped ('YES' or 'NO').
    - 'total' (float): The total cost of the order. This key is only present if 'shipped' is 'YES'.
    - 'carrier' (string): The shipping carrier for the order. This key is only present if 'shipped' is 'YES'.
    - 'tracking_number' (string): The tracking number for the order. This key is only present if 'shipped' is 'YES'.
    - 'delivered' (string): A string representing whether the order has been delivered ('YES' or 'NO'). This key is only
     present if 'shipped' is 'YES'.
    """
    orders = []
    for order in root.findall('Order'):
        order_dict = {
            'id': order.get('id'),
            'warehouse': order.get('warehouse'),
            'shipped': order.get('shipped')
        }
        if order_dict['shipped'] == 'YES':
            order_dict['total'] = float(order.get('total'))
            order_dict['carrier'] = order.find('TrackingNumber').get('carrier')
            order_dict['tracking_number'] = order.find('TrackingNumber').text
            order_dict['delivered'] = order.find('TrackingNumber').get('delivered')
        orders.append(order_dict)
    return orders


def display_orders(orders):
    """
    Displays the information for each order in the list of dictionaries returned by 'parse_orders'.

    Parameters:
    orders (list of dictionaries): A list of dictionaries, where each dictionary represents an order. Each dictionary should contain the following keys:
    - 'id' (string): The ID of the order.
    - 'warehouse' (string): The warehouse that the order is coming from.
    - 'shipped' (string): A string representing whether the order has been shipped ('YES' or 'NO').
    - 'total' (float): The total cost of the order. This key should only be present if 'shipped' is 'YES'.
    - 'carrier' (string): The shipping carrier for the order. This key should only be present if 'shipped' is 'YES'.
    - 'tracking_number' (string): The tracking number for the order. This key should only be present if 'shipped' is 'YES'.
    - 'delivered' (string): A string representing whether the order has been delivered ('YES' or 'NO'). This key should only be present if 'shipped' is 'YES'.
    """
    for order in orders:
        order_id = order['id']
        warehouse = order['warehouse']
        shipped = order['shipped']

        if shipped == 'YES':
            total = order['total']
            carrier = order['carrier']
            tracking_number = order['tracking_number']
            delivered = order['delivered']

            print(f"Order ID: {order_id}")
            print(f"Warehouse: {warehouse}")
            print(f"Total: {total}")
            print(f"Carrier: {carrier}")
            print(f"Tracking Number: {tracking_number}")
            print(f"Delivered: {delivered}")
        else:
            print(f"Order ID: {order_id}")
            print(f"Warehouse: {warehouse}")
            print("Order not yet shipped")
        print()  # Adds a newline after each order

if __name__ == '__main__':
    # Read the "tracking.xml" file
    tree = ET.parse('tracking.xml')
    root = tree.getroot()

    orders = parse_orders(root)
    display_orders(orders)

