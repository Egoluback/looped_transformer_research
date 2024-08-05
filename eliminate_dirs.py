import os, shutil

run_ids = ['0803162115-LR_loop_L1_ends{30}_T{15}-91e3',
 '0731160704-LR_loop_L3_ends{30}_T{15}-764c',
 '0730183917-LR_loop_L1_ends{30}_T{15}_N{11}-08ea',
 '0730200924-LR_loop_L1_ends{30}_T{15}_N{-1}-3aec',
 '0731110508-LR_loop_L1_ends{30}_T{15}_N{-1}-ebcd',
 '0805015441-LR_loop_L1_ends{30}_T{15}_N{-5}-c40c',
 '0801162621-LR_loop_L2_ends{30}_T{15}_N{-3}-d0d5',
 '0805012749-LR_loop_L1_ends{30}_T{15}_N{-7}-f037',
 '0805012838-LR_loop_L1_ends{30}_T{15}_N{-10}-9a65',
 '0805013143-LR_loop_L1_ends{30}_T{15}_N{0.7}-3fdf',
 '0805135822-LR_loop_L1_ends{30}_T{15}_N{0.8}-3171',
 '0801190515-LR_loop_L1_ends{30}_T{15}_N{-4}-4dc0',
 '0801140357-LR_loop_L1_ends{30}_T{15}_N{-2}-0f77',
 '0731012201-LR_loop_L1_ends{30}_T{15}_N{0.5}-aa1f',
 '0731105704-LR_loop_L1_ends{30}_T{15}_N{0.9}-ac48',
 '0731164711-LR_loop_L2_ends{30}_T{15}-d083',
 '0803162021-LR_loop_L2_ends{30}_T{15}-7ecd',
 '0803131927-LR_loop_L1_ends{30}_T{15}_ssm-ebc7',
 '0731142820-LR_loop_L3_ends{30}_T{15}-9d9e',
 '0804163507-LR_loop_L4_ends{30}_T{15}-0f3b',
 '0804163530-LR_loop_L4_ends{30}_T{15}_feed-c3c5',
 '0804163713-LR_loop_L2_ends{30}_T{15}_N{-3}-b580',
 '0801140714-LR_loop_L2_ends{30}_T{15}_feed-431f',
 '0803162000-LR_loop_L2_ends{30}_T{15}_feed-030b',
 '0801003556-LR_loop_L2_ends{30}_T{15}_feed-487d',
 '0801003556-LR_loop_L2_ends{30}_T{15}_feed-487d',
 '0805131259-LR_loop_L1_ends{30}_T{15}_skip-4455',
 '0805131337-LR_loop_L1_ends{30}_T{15}_N{-3}_skip-8d5e',
 '0805132432-LR_loop_L1_ends{30}_T{15}_N{-7}_skip-6103']

subfolders = [f.path for f in os.scandir(".") if f.is_dir() and f.path[2 :] not in run_ids]

for dir in subfolders:
    shutil.rmtree(dir)

print(f"{len(subfolders)} dirs removed.")
