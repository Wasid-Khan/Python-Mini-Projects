import PyPDF2
import os


def list_pdfs():
    """List all PDF files in the current directory."""
    pdf_files = [file for file in os.listdir(os.curdir) if file.endswith(".pdf")]
    if not pdf_files:
        print("No PDF files found in the current directory.")
    return pdf_files


def merge_pdfs(selected_files):
    """Merge selected PDF files."""
    merger = PyPDF2.PdfMerger()
    for file in selected_files:
        merger.append(file)
    output_file = input("Enter the name for the merged PDF (e.g., merged.pdf): ").strip()
    merger.write(output_file)
    merger.close()
    print(f"PDFs merged successfully into {output_file}!")


def split_pdf_interactive():
    """Split a selected PDF file into two parts based on user input."""
    pdf_files = list_pdfs()
    if not pdf_files:
        return  # Exit if no PDFs are available

    # Step 1: Display available PDFs and let the user select one
    print("Available PDFs:")
    for i, pdf in enumerate(pdf_files, start=1):
        print(f"{i}. {pdf}")

    selected_index = int(input("Enter the number of the PDF to split: ").strip()) - 1
    if selected_index < 0 or selected_index >= len(pdf_files):
        print("Invalid selection. Please try again.")
        return

    selected_pdf = pdf_files[selected_index]

    # Step 2: Check the number of pages in the selected PDF
    with open(selected_pdf, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf)
        total_pages = len(reader.pages)
        print(f"The selected PDF has {total_pages} pages.")

    split_page = int(input("Enter the page number to split the PDF at: ").strip())
    if split_page < 1 or split_page >= total_pages:
        print(f"Invalid page number. Please choose between 1 and {total_pages - 1}.")
        return

    # Step 3: Split the PDF into two parts
    with open(selected_pdf, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf)

        # Create the first part
        writer1 = PyPDF2.PdfWriter()
        for page in range(split_page):
            writer1.add_page(reader.pages[page])
        part1_file = f"{os.path.splitext(selected_pdf)[0]}_part1.pdf"
        with open(part1_file, 'wb') as part1_pdf:
            writer1.write(part1_pdf)
        print(f"Created: {part1_file}")

        # Create the second part
        writer2 = PyPDF2.PdfWriter()
        for page in range(split_page, total_pages):
            writer2.add_page(reader.pages[page])
        part2_file = f"{os.path.splitext(selected_pdf)[0]}_part2.pdf"
        with open(part2_file, 'wb') as part2_pdf:
            writer2.write(part2_pdf)
        print(f"Created: {part2_file}")

    print("PDF split successfully!")


def reorder_pages(pdf_file):
    """Reorder pages in a PDF."""
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf)
        num_pages = len(reader.pages)
        print(f"This PDF has {num_pages} pages.")
        order = input(
            "Enter the new page order separated by commas (e.g., 3,1,2): ").strip()
        order = [int(i) - 1 for i in order.split(",")]  # Convert to zero-based index
        writer = PyPDF2.PdfWriter()
        for page_num in order:
            writer.add_page(reader.pages[page_num])
        output_file = f"{os.path.splitext(pdf_file)[0]}_reordered.pdf"
        with open(output_file, 'wb') as output_pdf:
            writer.write(output_pdf)
        print(f"Pages reordered successfully into {output_file}!")


def main():
    print("Welcome to the PDF Utility Application!")
    while True:
        print("\nAvailable PDFs:")
        pdf_files = list_pdfs()
        for i, pdf in enumerate(pdf_files, start=1):
            print(f"{i}. {pdf}")

        print("\nOptions:")
        print("1. Merge PDFs")
        print("2. Split a PDF")
        print("3. Reorder pages in a PDF")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            if len(pdf_files) < 2:
                print("At least two PDFs are required to merge.")
            else:
                selected_indices = input(
                    "Enter the numbers of the PDFs to merge, separated by commas (e.g., 1,2): ").strip()
                selected_files = [pdf_files[int(i) - 1] for i in selected_indices.split(",")]
                merge_pdfs(selected_files)

        elif choice == "2":
            if not pdf_files:
                print("No PDFs available to split.")
            else:
                split_pdf_interactive()

        elif choice == "3":
            if not pdf_files:
                print("No PDFs available to reorder.")
            else:
                selected_file = input("Enter the number of the PDF to reorder: ").strip()
                reorder_pages(pdf_files[int(selected_file) - 1])

        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
