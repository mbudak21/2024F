{
  pkgs ? import (fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-23.11") { },
}:

pkgs.mkShellNoCC {
  packages = with pkgs; [
    (python3.withPackages (ps: [
      ps.pytorch
      ps.torchvision
      ps.torchaudio
      ps.pytorch-cuda
      ps.matplotlib
      ps.numpy
      ps.plotly
    ]))
    curl
    jq
    python311Packages.python-lsp-server
  ];
}
