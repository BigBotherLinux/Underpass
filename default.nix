{ pkgs ? import <nixpkgs> {} }:

pkgs.stdenv.mkDerivation {
  name = "underpass-font";

  src = ./.;

  buildInputs = [ pkgs.python3 pkgs.python3Packages.fonttools pkgs.yq ];

  installPhase = ''
    mkdir -p $out/share/fonts/truetype
    find $src -type f -name "*.ttf" | while read file; do
      echo "Processing $(basename "$file" .ttf)"
      python3 $src/convert_font.py "$file" "$out/share/fonts/truetype"
    done
    mkdir -p $out/share/fonts/opentype
    find $src -type f -name "*.otf" | while read file; do
      echo "Processing $(basename "$file" .otf)"
      python3 $src/convert_font.py "$file" "$out/share/fonts/opentype"
    done
  '';

  meta = {
    description = "A script to convert fonts to lowercase versions";
    maintainers = with pkgs.lib.maintainers; [ your_name ];  # Replace with your name
  };
}
