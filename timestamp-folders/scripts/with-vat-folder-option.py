import os

def get_user_choice(prompt, options):
    """
    Helper function to get a valid user choice from a list of options.
    """
    while True:
        print(prompt)
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")
        choice = input("Enter your choice (number): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        else:
            print("Invalid choice. Please try again.")

def get_years_selection():
    """
    Helper function to allow the user to select multiple years.
    """
    available_years = ["24", "25", "26", "27", "28", "29", "30"]
    print("Select the years you'd like to create folders for (separate multiple choices with commas):")
    print(", ".join(available_years))
    while True:
        selected_years = input("Enter your selections: ").strip().split(",")
        selected_years = [year.strip() for year in selected_years]
        if all(year in available_years for year in selected_years):
            return selected_years
        else:
            print("Invalid selection. Please choose from the available years.")

def create_folders(base_path, years, structure, include_vat_subfolders):
    """
    Creates folders based on the specified structure, optionally including VAT-related subfolders.
    """
    months = [
        ("01", "Jan"), ("02", "Feb"), ("03", "Mar"), ("04", "Apr"),
        ("05", "May"), ("06", "Jun"), ("07", "Jul"), ("08", "Aug"),
        ("09", "Sep"), ("10", "Oct"), ("11", "Nov"), ("12", "Dec")
    ]
    
    vat_subfolders = ["VAT-Deductible", "Non-VAT-Deductible"]
    
    for year in years:
        year_folder = os.path.join(base_path, year)
        
        try:
            os.makedirs(year_folder, exist_ok=True)  # Create the parent folder for the year
            print(f"Created/Verified: {year_folder}")
        except Exception as e:
            print(f"Error creating {year_folder}: {e}")
            continue
        
        # Create subfolders for each month
        for month_num, month_abbr in months:
            if structure == "MM":
                subfolder_name = f"{month_num}"
            elif structure == "MM-Month":
                subfolder_name = f"{month_num}-{month_abbr}"
            else:
                raise ValueError("Invalid folder structure.")
            
            month_folder_path = os.path.join(year_folder, subfolder_name)
            
            try:
                os.makedirs(month_folder_path, exist_ok=True)
                print(f"Created: {month_folder_path}")
                
                # Add VAT-related subfolders if requested
                if include_vat_subfolders:
                    for vat_subfolder in vat_subfolders:
                        vat_folder_path = os.path.join(month_folder_path, vat_subfolder)
                        os.makedirs(vat_folder_path, exist_ok=True)
                        print(f"Created: {vat_folder_path}")
            
            except Exception as e:
                print(f"Error creating {month_folder_path}: {e}")

def main():
    """
    Main function to interact with the user and generate folders.
    """
    print("Welcome to the Folder Generator Script!")
    
    # Get folder structure preference
    structure_prompt = (
        "Choose the subfolder naming structure:"
    )
    structure_options = ["MM (e.g., 01)", "MM-Month (e.g., 01-Jan)"]
    chosen_structure = get_user_choice(structure_prompt, structure_options)
    
    # Map user-friendly choice to internal representation
    if chosen_structure == "MM (e.g., 01)":
        folder_structure = "MM"
    elif chosen_structure == "MM-Month (e.g., 01-Jan)":
        folder_structure = "MM-Month"
    
    # Ask whether VAT-related subfolders should be included
    vat_prompt = (
        "Would you like to add 'VAT-Deductible' and 'Non-VAT-Deductible' subfolders "
        "within each month's folder?"
    )
    vat_options = ["Yes", "No"]
    include_vat_subfolders = get_user_choice(vat_prompt, vat_options) == "Yes"
    
    # Get system path from the user
    while True:
        base_path = input("Enter the system path where folders should be created: ").strip()
        if os.path.exists(base_path):
            break
        else:
            print("The specified path does not exist. Please try again.")
    
    # Get years selection
    selected_years = get_years_selection()
    
    # Create folders based on user input
    create_folders(base_path, selected_years, folder_structure, include_vat_subfolders)
    
    print("Folder generation complete!")

if __name__ == "__main__":
    main()
