// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MyToken is ERC20, Ownable {
    constructor() ERC20("blockdrive_", "Bd") {}

    struct File {
        bytes32 filename;
        bytes32 cid;
    }

    mapping(address => File[]) public files;

    function addFile(address _owner, bytes32 _filename, bytes32 _cid) public onlyOwner {
        File memory file = File({
            filename: _filename,
            cid: _cid
        });

        files[_owner].push(file);
    }

    function getFile(address _owner, bytes32 _filename) public view returns (bytes32) {
        for (uint i = 0; i < files[_owner].length; i++) {
            if (files[_owner][i].filename == _filename) {
                return files[_owner][i].cid;
            }
        }

        return 0x0;
    }

    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }
}
