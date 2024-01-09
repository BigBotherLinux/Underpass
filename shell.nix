{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python3
    pkgs.python3Packages.fonttools
  ];

  shellHook = ''
    echo "Run the script with: python convert_font.py <font-file>"
  '';
}

