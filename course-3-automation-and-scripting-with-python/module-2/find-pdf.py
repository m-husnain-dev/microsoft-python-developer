import glob

# Search for all PDF files in 'documents' and its subdirectories
pdf_files = glob.glob('documents/**/*.pdf', recursive=True)

# Display the list of full file paths
print(pdf_files)