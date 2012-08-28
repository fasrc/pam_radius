pam_radius
==========

Customized Pam-Radius SRPM and Spec file

This is a very simple patched RPM, patched to change the prompt "Password:" to "Verification code:" 

We have included the SRPM, SPEC file, and patch here, though of course the SRPM contains all of this is and ready to build. 

This is used in conjunction with FAS RC Openauth 2 factor authentication system. This pam_radius pam module would be installed on clients of the OpenAuth Radius Servers (login nodes/vpn endpoints etc)

