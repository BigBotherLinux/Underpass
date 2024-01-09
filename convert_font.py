from fontTools.ttLib import TTFont
import sys
import os.path

def convert_to_lowercase(font_path, dest_path):
    font = TTFont(font_path)

    # Define the ranges of uppercase characters with a +32 offset
    standard_uppercase_ranges = [(65, 90), (192, 223), (1040, 1071)]  # Add more ranges if needed

    # Define the ranges of characters where every alternate character needs a +1 offset
    alternate_uppercase_ranges_even = [(256, 311), (313, 328), (330, 375), (377, 382), (461, 476), (478,495), (504, 539), (550, 563), (1122, 1228), (1232, 1309),(7684,7827),(7840,7929)]  # Fill in with actual ranges


    for table in font['cmap'].tables:
        new_cmap = {}
        for char_code, glyph_name in table.cmap.items():
            new_char_code = None

            # Check if the character is in the standard range
            if any(lower <= char_code <= upper for lower, upper in standard_uppercase_ranges):
                new_char_code = char_code + 32
            
            # Check if the character is in the alternate range
            for lower, upper in alternate_uppercase_ranges_even:
                if lower <= char_code <= upper:
                    # Apply +1 offset to every alternate character
                    if (char_code - lower) % 2 == 0:
                        new_char_code = char_code + 1
                    break  # Exit the loop once a matching range is found

            # Perform the replacement if a new character code was calculated
            if new_char_code is not None:
                lower_glyph_name = table.cmap.get(new_char_code)
                if lower_glyph_name:
                    new_cmap[char_code] = lower_glyph_name
            else:
                # Keep the original mapping for other characters
                new_cmap[char_code] = glyph_name
        
        table.cmap = new_cmap

    new_font_path = dest_path + '/' +  os.path.basename(font_path.replace(".ttf", "_lowercase.ttf").replace(".otf", "_lowercase.otf").replace("Overpass", "Underpass"))
    font.save(new_font_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <font_file> <dest_folder>")
    else:
        font_file = sys.argv[1]
        dest_file = sys.argv[2]
        convert_to_lowercase(font_file, dest_file)
