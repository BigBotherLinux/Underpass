{
  description = "A flake for the Underpass font conversion";

  inputs = {
    nixpkgs.url = "nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
        underpass-font = pkgs.callPackage ./default.nix { };
      in
      {
        packages.underpass-font = underpass-font;
        defaultPackage = underpass-font;
      }
    );
}
