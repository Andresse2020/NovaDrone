import os
import glob

# === CONFIGURATION ===
MAIN_DIR = "BassingaLib"  # Path to your main library directory

# Output filenames
SYM_OUTPUT_FILE = "sym-lib-table"
FP_OUTPUT_FILE = "fp-lib-table"

# === GENERATE sym-lib-table (Symbol libraries) ===
print("Generating symbol library table...")
sym_files = list(glob.glob(os.path.join(MAIN_DIR, "**", "*.kicad_sym"), recursive=True))

with open(SYM_OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write("(sym_lib_table\n")
    f.write("  (version 7)\n")
    
    for file_path in sym_files:
        # Get filename without extension
        filename = os.path.basename(file_path)
        lib_name = os.path.splitext(filename)[0]
        
        # Calculate relative path for URI
        relative_uri = os.path.relpath(file_path).replace("\\", "/")
        
        # Generate library entry
        f.write(f'  (lib (name "{lib_name}")(type "KiCad")(uri "${{KIPRJMOD}}/{relative_uri}")(options "")(descr ""))\n')
    
    f.write(")\n")

# === GENERATE fp-lib-table (Footprint libraries) ===
print("Generating footprint library table...")
# Find all .pretty directories (footprint libraries)
pretty_dirs = []
for root, dirs, _ in os.walk(MAIN_DIR):
    for dir_name in dirs:
        if dir_name.endswith('.pretty'):
            pretty_dirs.append(os.path.join(root, dir_name))

with open(FP_OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write("(fp_lib_table\n")
    f.write("  (version 7)\n")
    
    for dir_path in pretty_dirs:
        # Get directory name without .pretty extension
        dir_name = os.path.basename(dir_path)
        lib_name = dir_name.replace('.pretty', '')
        
        # Calculate relative path for URI
        relative_uri = os.path.relpath(dir_path).replace("\\", "/")
        
        # Generate library entry
        f.write(f'  (lib (name "{lib_name}")(type "KiCad")(uri "${{KIPRJMOD}}/{relative_uri}")(options "")(descr ""))\n')
    
    f.write(")\n")

# === SUMMARY ===
print("\n=== GENERATION COMPLETE ===")
print(f"Symbol libraries: {len(sym_files)} found -> '{SYM_OUTPUT_FILE}'")
print(f"Footprint libraries: {len(pretty_dirs)} found -> '{FP_OUTPUT_FILE}'")

# Show lists
if sym_files:
    print("\nSymbol libraries (.kicad_sym):")
    for sf in sym_files:
        print(f"  - {os.path.basename(sf)}")
        
if pretty_dirs:
    print("\nFootprint libraries (.pretty):")
    for pd in pretty_dirs:
        print(f"  - {os.path.basename(pd)}")
