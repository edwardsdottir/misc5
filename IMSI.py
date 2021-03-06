U
    �
`v  �                
   @   s�   d dl T d dlZd dlZdZdddddd	d
ddd�	Zdd� Zdd� Zdd� Zdd� Ze	� Z
e
�dd� e
�d� ee
�Ze
jed� ee�Zejded� ejded� e��  ejded� ee
dedd �Zejeed!� e
��  dS )"�    )�*NFl   mL�" l   �wUO�f l   �!\j$ l   !��: l   '�+�l   `&�/�tl   s�H�J l   <f��Y l   �.�s�: )	�Device 1�Device 2�Device 3�Device 4�Device 5�Device 6�Device 7�Device 8�Device 9c                  C   sn   t dd�D ]@} tjdt| d � d d� t��  | dkr@t�  t�d� q
t	�
d� tjd	d� t��  d S )
Nr   �   zJamming A2G signal...�
   �%��textg      �?�Jam A2GzJamming Complete.)�range�updateMe�config�str�root�update�createButtons�time�sleep�subMenu�delete)�i� r   �tkintertest.py�updateLabel   s    
r    c                 C   s*   t jd�| �tt|  � d� t��  d S )Nz{}'s IMSI is: r   )r   r   �formatr   �imsiNumsr   r   )Zdevicer   r   r   �ping%   s    r#   c            
      C   s8  t d� tdd�D ](} tjd�| �d� t��  t�d� qt	tdt
td � dd	�}|jttd
� t�d� t��  t	tdt
td � dd	�}|jttd
� t�d� t��  t	tdt
td � dd	�}|jttd
� t�d� t��  t	tdt
td � dd	�}|jttd
� t�d� t��  t	tdt
td � dd	�}|jttd
� t�d� t��  t	tdt
td � dd	�}|jttd
� t�d� t��  t	tdt
td � dd	�}|jttd
� t�d� t��  t	tdt
td � dd	�}|jttd
� t�d� t��  t	tdt
td � dd	�}	|	jttd
� d S )Nzpinging all devices�   r   zPinging device {}r   zDevice 1's IMSI is: r   )�Arial�   )r   �font��sideZfillg      �?zDevice 2's IMSI is: r   zDevice 3's IMSI is: r   zDevice 4's IMSI is: r   zDevice 5's IMSI is: r   zDevice 6's IMSI is: r   zDevice 7's IMSI is: r	   zDevice 8's IMSI is: r
   zDevice 9's IMSI is: r   )�printr   r   r   r!   r   r   r   r   �Labelr   r"   �pack�TOP�BOTH)
r   Zlabel1Zlabel2Zlabel3Zlabel4Zlabel5Zlabel6Zlabel7Zlabel8Zlabel9r   r   r   �pingAll)   sN    







r/   c            
      C   s>  t tddd� d�} | jtd� t tddd� d�}|jtd� t tdd	d� d�}|jtd� t td
dd� d�}|jtd� t tddd� d�}|jtd� t tddd� d�}|jtd� t tddd� d�}|jtd� t tddd� d�}|jtd� t tddd� d�}|jtd� tt�}	tjd|	d� |	jdtd� t	�
�  d S )NZDevice1c                   S   s   t d�S )Nr   �r#   r   r   r   r   �<lambda>T   �    zcreateButtons.<locals>.<lambda>)r   �command)r)   ZDevice2c                   S   s   t d�S )Nr   r0   r   r   r   r   r1   V   r2   ZDevice3c                   S   s   t d�S )Nr   r0   r   r   r   r   r1   X   r2   ZDevice4c                   S   s   t d�S )Nr   r0   r   r   r   r   r1   Z   r2   ZDevice5c                   S   s   t d�S )Nr   r0   r   r   r   r   r1   \   r2   ZDevice6c                   S   s   t d�S )Nr   r0   r   r   r   r   r1   ^   r2   ZDevice7c                   S   s   t d�S )Nr	   r0   r   r   r   r   r1   `   r2   ZDevice8c                   S   s   t d�S )Nr
   r0   r   r   r   r   r1   b   r2   ZDevice9c                   S   s   t d�S )Nr   r0   r   r   r   r   r1   d   r2   ZPing��label�menuzPing All Devices�r5   r3   )ZButtonr   r,   ZLEFT�Menu�topMenu�add_cascade�add_commandr/   r   �add_separator)
Zbutt1Zbutt2Zbutt3Zbutt4Zbutt5Zbutt6Zbutt7Zbutt8Zbutt9ZsubMenu2r   r   r   r   S   s,    r   i�  zChallenge 4)r6   ZJamr4   r   r7   ZExitzWelcome to Jam and Capture v1.0)r%   �   )r   Zreliefr'   r(   )Ztkinterr   ZrandomZjammedr"   r    r#   r/   r   ZTkr   Zminsize�titler8   r9   r   r   r:   r;   r<   �exitr+   ZSUNKENr   r,   r-   r.   Zmainloopr   r   r   r   �<module>   s<   �*
