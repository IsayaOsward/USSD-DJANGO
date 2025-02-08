def ussd_menu(session, user_input):
    # List of some of mobile Team Products
    products = [
        {"name": "Kakakuona Oxygen", "description": "This is a cross-platform chat application commonly used at eGA RIDC."},
        {"name": "e-Barua", "description": "This is a mailing application used to send and receive emails using the eGA-specific domain mail addresses."},
        {"name": "Duma VPN", "description": "This is a virtual private network mobile application for both Android and iOS devices."},
        {"name": "eMrejesho", "description": "This is another mobile application used by Tanzania government and citizens to deliver their complaints, feedbacks, and track their progressions."},
        {"name": "Twiga Cloud", "description": "This is a mobile application also available for web, which serves as an online storage system like popular ones such as Google Drive."},
        {"name": "eMikutano", "description": "This is a mobile application used to join and participate in online meetings."},
        {"name": "eBoard", "description": "This is an application for managing board meetings and other related activities, available on both mobile and desktop."}
    ]
    
    # List of team members with roles and phone numbers
    members = [
        {"name": "Germnanus Xavier", "role": "Team Leader", "phone": "To Be Added"},
        {"name": "John Malugu", "role": "Senior Leader", "phone": "To Be Added"},
        {"name": "Rojasy Ngaiza", "role": "Team Member", "phone": "To Be Added"},
        {"name": "Joyce Kimata", "role": "Team Member", "phone": "To Be Added"},
        {"name": "Bernard Augustin", "role": "Team Member", "phone": "To Be Added"},
        {"name": "Neema Kamugisha", "role": "Team Member", "phone": "To Be Added"},
        {"name": "Fred Herbert", "role": "Team Member", "phone": "To Be Added"},
        {"name": "Michael Michael", "role": "Team Member", "phone": "To Be Added"},
        {"name": "Isaya Osward", "role": "Team Member", "phone": "255755957514"},
        {"name": "Daniel Kulwa", "role": "Team Member", "phone": "To Be Added"},
        {"name": "Karen Mwaibindi", "role": "Team Member", "phone": "To Be Added"},
        {"name": "Agripina Mvungi", "role": "Team Member", "phone": "To Be Added"},
        {"name": "Paulo Michael", "role": "Team Member", "phone": "To Be Added"},
        {"name": "Paul Kingwa", "role": "Team Member", "phone": "To Be Added"},
        {"name": "Melckizedeck", "role": "Team Member", "phone": "To Be Added"}
    ]

    #About eGA RIDC, Mobile Team
    about = """
    The eGA RIDC, Mobile Team, is one of the core unit at eGA RIDC which is responsible for developing, maintaining and publishing mobile application, desktop applications and sometimes web and backend systems which are used by eGA and public at large.
    """

    user_input = user_input.strip()
    input_parts = user_input.split('*')
    if len(input_parts) > 1:
        user_input = input_parts[-1]

    session["text"] = ""

    if session.get("state") == "welcome":
        session["name"] = user_input
        session["state"] = "main_menu"
        return f"Welcome {user_input}!\nChoose one among options below:\n1. About eGA-RIDC, Mobile Team\n2. Our Products\n3. Our Members", False

    elif session.get("state") == "main_menu":
        if user_input == "1":
            session["state"] = "about_team"
            return f"{about}.\n0. Go Back", False
        elif user_input == "2":
            session["state"] = "products"
            # Generating a list of product options dynamically
            products_list = "\n".join([f"{index + 1}. {product['name']}" for index, product in enumerate(products)])
            return f"Our Products:\n{products_list}\n0. Go Back", False
        elif user_input == "3":
            session["state"] = "members"
            # Generating a list of members dynamically
            members_list = "\n".join([f"{index + 1}. {member['name']}" for index, member in enumerate(members)])
            return f"Our Members:\n{members_list}\n0. Go Back", False
        else:
            return "Invalid choice. Please select an option:\n1. About eGA-Innovation Team\n2. Our Products\n3. Our Members", False

    elif session.get("state") == "about_team":
        if user_input == "0":
            session["state"] = "main_menu"
            return f"Welcome {session['name']}!\nChoose one among options below:\n1. About eGA-Innovation Team\n2. Our Products\n3. Our Members", False
        else:
            return "Invalid choice. Press 0 to go back.", False

    elif session.get("state") == "products":
        try:
            product_index = int(user_input) - 1
            if 0 <= product_index < len(products):
                session["state"] = "product_detail"
                session["product_id"] = product_index
                selected_product = products[product_index]
                return f"{selected_product['name']}:\n{selected_product['description']}\n0. Go Back", False
            elif user_input == "0":
                session["state"] = "main_menu"
                return f"Welcome {session['name']}!\nChoose one among options below:\n1. About eGA-Innovation Team\n2. Our Products\n3. Our Members", False
            else:
                return "Invalid choice. Please select a valid product or press 0 to go back.", False
        except ValueError:
            return "Invalid input. Please enter a valid number to select a product or press 0 to go back.", False

    elif session.get("state") == "product_detail":
        if user_input == "0":
            session["state"] = "products"
            # Generating a list of product options dynamically
            products_list = "\n".join([f"{index + 1}. {product['name']}" for index, product in enumerate(products)])
            return f"Our Products:\n{products_list}\n0. Go Back", False
        else:
            return "Invalid choice. Press 0 to go back.", False

    elif session.get("state") == "members":
        try:
            member_index = int(user_input) - 1
            if 0 <= member_index < len(members):
                selected_member = members[member_index]
                member_name = selected_member['name']
                member_role = selected_member.get('role', 'Team Member')
                member_phone = selected_member.get('phone', 'Not available')
                return f"{member_name}\nRole: {member_role}\nPhone: {member_phone}\n0. Go Back", False
            elif user_input == "0":
                session["state"] = "main_menu"
                return f"Welcome {session['name']}!\nChoose one among options below:\n1. About eGA-Innovation Team\n2. Our Products\n3. Our Members", False
            else:
                return "Invalid choice. Please select a valid member or press 0 to go back.", False
        except ValueError:
            return "Invalid input. Please enter a valid number to select a member or press 0 to go back.", False

    else:
        session["state"] = "welcome"
        return "Welcome to eGA-RIDC, Mobile Team!\nPlease enter your name:", False
