# README

This repository illustrates the tool, data, and scripts of our ICSE2025 under-reviewing work —— `The Design Smells Breaking the Boundary between Android Variants and AOSP`.

We opened all of the collected data of the investigated open-source subjects.  Due to the file size limit of GitHub, we upload the processed data to this repository. Please connect us for the large-scale raw data if required.

The whole directory tree goes like the following:

```
│  README.md
│
├─Data
│  ├─Methodology
│  │  └─DroidDS-sample
│  │      ├─input
│  │      └─output
│  ├─Results
│  │  ├─RQ1
│  │  │  └─mc
│  │  │      ├─AOSPA
│  │  │      │  ├─quartz
│  │  │      │  ├─ruby
│  │  │      │  ├─sapphire
│  │  │      │  └─topaz
│  │  │      ├─CalyxOS
│  │  │      │  ├─android13
│  │  │      │  ├─android12
│  │  │      │  └─android11
│  │  │      ├─LineageOS
│  │  │      │  ├─lineage-20.0
│  │  │      │  ├─lineage-19.1
│  │  │      │  ├─lineage-18.1
│  │  │      │  ├─lineage-17.1
│  │  │      │  ├─lineage-18.1
│  │  │      │  └─lineage-16.0
│  │  │      ├─OmniROM
│  │  │      │  ├─android-13.0
│  │  │      │  ├─android-12.0
│  │  │      │  ├─android-11
│  │  │      │  ├─android-10
│  │  │      │  └─android-9
│  │  │      └─IndustrialX
│  │  │         ├─I-E
│  │  │         ├─I-D
│  │  │         ├─I-C
│  │  │         ├─I-B
│  │  │         └─I-A
│  │  ├─RQ2
│  │  │  ├─ConfF&ConfB
│  │  │  ├─ConfF&ConfB_cap
│  │  │  └─recur_block_cap
│  │  │      └─text-50%
│  │  │          ├─diff-commit
│  │  │          ├─diff-commit-times
│  │  │          ├─diff-project
│  │  │          ├─diff-project-times
│  │  │          ├─diff-version
│  │  │          └─diff-version-times
│  │  └─RQ3
│  │      └─mitigable
│  │          ├─AOSPA
│  │          │  ├─quartz
│  │          │  ├─ruby
│  │          │  ├─sapphire
│  │          │  └─topaz
│  │          ├─CalyxOS
│  │          │  ├─android13
│  │          │  ├─android12
│  │          │  └─android11
│  │          ├─LineageOS
│  │          │  ├─lineage-20.0
│  │          │  ├─lineage-19.1
│  │          │  ├─lineage-18.1
│  │          │  ├─lineage-17.1
│  │          │  └─lineage-16.0
│  │          └─OmniROM
│  │          │  ├─android13.0
│  │          │  ├─android-13.0
│  │          │  ├─android-12.0
│  │          │  ├─android-11
│  │          │  ├─android-10
│  │          │  └─android-9
│  │          └─IndustrialX
│  │             ├─I-E
│  │             ├─I-D
│  │             ├─I-C
│  │             ├─I-B
│  │             └─I-A
│  └─Setup
│      ├─Conflict_collection
│      │  ├─AOSPA
│      │  ├─CalyxOS
│      │  ├─LineageOS
│      │  └─OmniROM
│      └─Subject_collection
│          ├─AOSPA
│          ├─CalyxOS
│          ├─LineageOS
│          └─OmniROM
├─Method
└─Scripts
    ├─RQ_scripts
    │  ├─RQ1
    │  ├─RQ2
    │  └─RQ3
    └─setup_scripts
```

The video demo (speed up 16 times) website is at (upload soon).

## Method

### DroidDS

### Requirements

- Operating System : *Linux*
- `Python` 3.8 or higher.
- `Java Runtime Environment (JRE)` or `Java Development Kit (JDK)` version 21 or higher.

### Usage

To use `DroidDS`, run the script from the command line, specifying the necessary arguments. Here is a breakdown of the available arguments:

```less
usage: DroidDS [-h] [--memory ENRE_MAX_MEMORY] [--repo_extensive REPO_EXTENSIVE] [--repo_extensive_name REPO_EXTENSIVE_NAME] [--hidden_extensive HIDDEN_EXTENSIVE] [--repo_aosp REPO_AOSP] [--repo_aosp_name REPO_AOSP_NAME] [--hidden_aosp HIDDEN_AOSP] [--commit_extensive COMMIT_EXTENSIVE] [--commit_aosp COMMIT_AOSP] [--output OUTPUT]

arguments:
`--memory`, `-mem`: Specify the maximum memory usage of the Java Virtual Machine(JVM). Default is `16G`.
`--repo_extensive`, `-rpe`: Specify the Git repository path for the extensive AOSP.
`--repo_extensive_name`, `-rpen`: Specify the project name for the extensive AOSP repository.
`--hidden_extensive`, `-hde`: Specify the path to the CSV file containing extensive AOSP hidden flags.
`--repo_aosp`, `-rpa`: Specify the Git repository path for the AOSP project.
`--repo_aosp_name`, `-rpan`: Specify the project name for the AOSP repository.
`--hidden_aosp`, `-hda`: Specify the path to the CSV file containing AOSP hidden flags.
`--commit_extensive`, `-ce`: Specify the commit hash for the extensive AOSP project.
`--commit_aosp`, `-ca`: Specify the commit hash for the AOSP project.
`--output`, `-o`: Specify the root directory for output files.

eaxmple usage:
./DroidDS \\
  -rpe /data1/DroidDS/AndroidSourceCodeGit/L-18.1 \\
  -rpen L-18.1 \\
  -hde /data1/DroidDS/DroidDS-sample/input/hiddenapi-flags-L-18.1.csv \\
  -ce 7f7fc2562a95be630dbe609e8fb70383dcfada4f \\
  -rpa /data1/DroidDS/AndroidSourceCodeGit/aosp_android11 \\
  -rpan aosp_android11 \\
  -hda /data1/DroidDS/DroidDS-sample/input/hiddenapi-flags-android11.csv \\
  -ca 49d8b986dddd441df741698541788c5f3a9c465f \\
  -o /data1/DroidDS/DroidDS-sample/output
```

### Additional Notes

- `DroidDS` requires high performance, so we've set the `JVM` memory to a default of `16GB` to prevent heap overflow.
- When using the command-line arguments `rpe` and `rpen` (same as `rpa` and `rpan`)with the provided tool, it's important to ensure that the value for `rpen(-rpan)` (representing the name of the project) directly corresponds to the last segment of the path provided to `rpe(-rpa)`(representing the repository path).
- The `-hidden_extensive -hde` and `-hidden_aosp -hda` arguments are optional.
    - However, omitting these options might impact the accuracy or completeness of detection results, particularly in relation to specific aspects denoted by "XX", "XX", and "XX".
- `DroidDS` may takes a long time to run, as indicated by its 85-minute duration in the mentioned `DroidDS-sample` project.

## Scripts

### Setup (Section III.C Conflict Collection)

### Collecting Merge Conflicts

You can refer to the `README` of [depFCD](https://github.com/DepFCD/DepFCD)  (in the [Set up]((%3Chttps://github.com/DepFCD/DepFCD?tab=readme-ov-file#scripts%3E)))for the process of collecting merge conflicts.

### Collecting Recurring Merge Conflicts

The following are the main steps for collecting recurring merge conflicts:

***Step 1:***  `[process_conf_text.py](Scripts/setup_scripts/process_conf_text.py)`. This script automatically reverts the target repository to the parent commit state involved in the conflict and extracts the conflict text information.

- *Input*: A `CSV` file that records the details of the conflicting blocks.
- *Output*: `JSON` file containing text information corresponding to each conflicting block.

***Step 2:***  Execute the [recur_text_conf_search_commit.py](Scripts/setup_scripts/recur_text_conf_search_commit.py) or [recur_text_conf_search_diffversion.py](Scripts/setup_scripts/recur_text_conf_search_diffversion.py)  to detect duplicate conflict blocks across commits (or across versions, projects).

- *Input*: The `JSON` file produced in ***Step 1***.
- *Output*: `CSV` file containing details of duplicate conflict blocks.

***Step 3:***  Execute [conf_recur_times.py](Scripts/setup_scripts/conf_recur_times.py) to get the number of collisions for each conflicting block.

- *Input*: The `CSV` file generated in ***Step 2***.
- *Output*: `CSV` file containing the number of repeated collisions.

### RQ1

The `compute_avg_measures.py` is to compute value for files infected by design smells and that for non-infected files and `compute_wilcoxon.py` is to do Wilcoxon test based on each group of (avg_mc_aff, avg_mc_aff ).

```less
take DroidDS-sample's output as an eaxmple usage
python compute_avg_measures.py
python compute_wilcoxon.py
```

- *Input*:
    1. `all_aff_files.csv` , it is one of the output results from `DroidDS` and the column names are `project` , `aff_files`, `aff_files_count`. For detailed information, please refer to the part of Data/Methodology/output[].
    2. `file-ext_mc.csv`, it is one of the output results from `DroidDS` and the column names are `filename`, `#author`, `#cmt`,`changeloc`,`#issue`,`#issue-cmt`,`issueLoc`. For detailed information, please refer to the part of Data/Methodology/output[].
- *Output:*
    - `metrics.csv`: the column names are `project`,`avg_mc_aff`,`avg_mc_nonaff`,which indicating the average maintenance cost (i.e., avg_mc_aff ) of the files involved in design smells and the average values (i.e., avg_mc_nonaff ) of other files in terms of each measure.
    - `Wilcoxon-output.csv` : the column names are `project` , `P-value`, `increase`,which indicating the results of Wilcoxon Sign-Rank tests based on each group of (avg_mc_aff, avg_mc_aff ).

### RQ2

- ***Step 1*** : Run `andro_base_branch_commit_hist.py` to retrieve commit history.
    - Input: Path to the project's base repository and all branch versions of the repository.
    - Output: A text file that stores all the commit history.
- ***Step 2*** : Run `merge_extract.py` to acquire all merge points.
    - Input: The branches of Android variants and AOSP.
    - Output: The merge points of Android variants and AOSP.
- ***Step 3*** : Run `merge_conf_ast.py` to get the details of conflict blocks.
    - Input: Path to the base repository of Android variants and AOSP.
    - Output: A CSV file stores information about conflict blocks.
- ***Step 4*** : Run `process_conf_meths.py` to obtain detailed information on conflict blocks.
    - Input: A file called `project-version-merge.csv` generated from ***Step 3***.
    - Output: A CSV file stores detailed information on conflict blocks.
- ***Step 5*** : Run `conf_meths_cap.py` to obtain conflict information involving design smells.
    - Input: The CSV file produced in the fourth step.
    - Output: A CSV file stores conflict information involving design smells.

### RQ3

The `filter_mitigable.py` is used to assess whether a design smell instance is mitigable. 

```less
take DroidDS-sample's output as an eaxmple usage
python filter_mitigable.py
```

- *Input*:
    - `res_metric_statistic.json` , it is one of the output results from `DroidDS`.
- *Output:*
    - `mitigable_count.csv`: the column names are `project`,`smell_mitigable`,`smell_notMitigable`, which indicating project name, the kind of smell, count of mitigable or not mitigable smell instance.

## Data

### Methodology

To better illustrate the input and output of `DroidDS`, we provided an sample project `DroidDS-sample`. 

`Operating System` : Ubuntu 18.04.1

`Input argument explanation`

The Android variant version of the sample project is LineageOS-lineage-18.1, and its source code of `platform/frameworks/base` is in `/data1/DroidDS/AndroidSourceCodeGit/L-18.1`(i.e. the input of `-rpe` argument). The final directory is L-18.1 (i.e. the input of `-rpen` argument). Its hidden-flags is `/data1/DroidDS/DroidDS-sample/input/hiddenapi-flags-L-18.1.csv` (i.e. the input of `-hde` argument). Its commitId is `7f7fc2562a95be630dbe609e8fb70383dcfada4f` (i.e. the input of `-ce` argument). 

The corresponding AOSP version of the sample project is AOSP-android11, and its source code of `platform/frameworks/base` is in `/data1/DroidDS/AndroidSourceCodeGit/`aosp_android11 (i.e. the input of `-rp`a argument). The final directory is aosp_android11  (i.e. the input of `-rpea` argument). Its hidden-flags is `/data1/DroidDS/DroidDS-sample/input/hiddenapi-flags-android11.csv` (i.e. the input of `-hd`a argument). Its commitId is `49d8b986dddd441df741698541788c5f3a9c465f` (i.e. the input of `-ce` argument). 

The outputs of `DroidDS-sample` is `/data1/DroidDS/DroidDS-sample/output`(i.e. the input of `-o` argument).

It should be noted that due to the large scale of the Android system's code, we are unable to upload the complete project source code to the GitHub repository. 

So, the example usage is : 

```less
./DroidDS \\
  -rpe /data1/DroidDS/AndroidSourceCodeGit/L-18.1 \\
  -rpen L-18.1 \\
  -hde /data1/DroidDS/DroidDS-sample/input/hiddenapi-flags-L-18.1.csv \\
  -ce 7f7fc2562a95be630dbe609e8fb70383dcfada4f \\
  -rpa /data1/DroidDS/AndroidSourceCodeGit/aosp_android11 \\
  -rpan aosp_android11 \\
  -hda /data1/DroidDS/DroidDS-sample/input/hiddenapi-flags-android11.csv \\
  -ca 49d8b986dddd441df741698541788c5f3a9c465f \\
  -o /data1/DroidDS/DroidDS-sample/output
```

`TimeCost` : one and half hour

The video demo (speed up 16 times) website is at 

This `Data/Methodology/DroidDS-sample/output`directory contains the data of ownership, dependencies information, maintenance cost, design smell detection result and files affected by design smells generated by `DroidDS`. Below is an introduction to the content of each file.

- `all_aff_files.csv` : the file list which affected by design smells.
- `dependencies.csv` : the result of dependencies between AOSP and AOSP variant.
- `entities_ownership.csv` : the entity ownership detection result below the 'File' level in the project.
- `file-mc_ext.csv` : the maintenance cost for each file computed by `author`, `commit`,`changeloc`,`issue` ,`#issue-cmt`,`issueLoc`
- `L-18.1-CD4.csv` : the detection result of CD4.
- `res.json` : the detection  result of other ID1-ID4, UD1-UD5, CD1-CD4.
- `res_metric_statistic.json` : the midden result used to judge one smell instance is `isMitigable` .

### Setup

The folder contains initial data necessary to conduct experiments and investigate four research questions.

### Subject Collection

This directory contains merge points in which downstream project versions merge upstream AOSP

- `<project name>-<version>-merge.csv` : the merge points of the current downstream project version which contains merge commit, both upstream and downstream's parent commits and branches.

### Conflict Collection

This directory contains data on textual conflict detection results of each project version and details of manually selected conflict blocks.

- `<project name>-<version>-merge.csv` : the conflict details of the current downstream project version which contains merge nodes, conflict files quantity, conflict java files quantity, and conflict blocks LOC.

### Results

### RQ1: Do entities involved in design smells consume more maintenance costs than other entities in Android variants?

All files mentioned below are in /Data/Results/RQ1.

The content of `all_aff_files.csv` is the file list affected by design smells in each project.

The content of `Figure 4.csv` is the original data of `Figure 4`.

The content of `Table 3.csv` is  the original data of `Table 3`.

### The files in `mc` are the original files generated by `DroidDS`, and each `file-mc_ext.csv` in {project}/{verison} directory records the maintenance cost for each file computed by`author`, `commit`,`changeloc`,`issue` ,`#issue-cmt`,`issueLoc`.

### RQ2: To what extent do the entities involved in design smells capture conflicts due to Android variants merging with AOSP changes?

All files or directories mentioned below are in Data/Results/RQ2.

### The files in `ConfF&ConfB` are generated by RQ2 Step 4, and each `project-version-meths.csv` file records the conflict block information of the project that has occurred conflict merge several times.

- `Merge`: The commit id on which the merge conflict occurred
- `Conf_detail`: The file in conflict
- `Loc`: The total number of conflict lines in the file
- `Block`: The number of conflicting blocks in the file
- `Loc_details`: The location information for each conflicting block, including the start line number and the total number of lines.

### The files in `ConfF&ConfB_cap` are generated by RQ2 step 5. Each `project-version-meths.csv` file records the conflict block information of several conflict merges in the project, and these conflicts are caused by anti-patterns.

- `Merge` : The commit id on which the merge conflict occurred
- `Conf_detail`: The file where the conflict occurred
- `Loc`: The total number of lines of code in the conflict block of the file
- `Block` : The number of conflicting blocks in the file
- `Loc_details` : Location information for each conflicting block, including the start line number and total line number.
- `is_in_aff_files` : Used to indicate if the conflict is related to the antipattern, "True".

### `recur_block_cap` is used to record repeated conflict blocks across commits, versions, and projects when the threshold is set to 50%.

- The files in `diff-commit`, `diff-version`, and `diff-project` are derived from steps 1 and 2 of Set up 3.3. Here's an explanation of the fields in each `progect-cap-recur_textblock.csv` file:
    - `merge_commitid`: The commitid on which the merge conflict occurred.
    - `file`: The file in which the conflict occurred.
    - `Loc_details`: Location information for each conflicting block, including the start line number and total line number.
    - `block_text_num`; : Text information for the conflicting block.
    - `recur_segment`: two similar text segments that repeat conflicting blocks.
    - `proportion` : the proportion of similar text segments in each conflicting block.
- The files in `diff-commit-times`, `diff-version-times`, and `diff-project-times` are derived from step three of Setup. Here's an explanation of the fields in each `progect-cap-recur_textblock.csv` file:
    - `file` : The file in which the conflict occurred.
    - `merge_commitid` : The commitid on which the merge conflict occurred.
    - `recur_segment` : two similar text segments that repeat conflicting blocks.
    - `times` : the total number of times each conflict block occurs across commits/versions/projects.

### RQ3: To what extent can design smell instances be mitigable to promote Android variant maintainability?

All files or directories mentioned below are in Data/Results/RQ3

The content of `Table 7.csv` is  the original data of `Table 7`.

The content of `Table 8.csv` is  the original data of `Table 8`.

### The files in `mitigable` are the original files generated by `DroidDS`, and each `res_metric_statistic.json` in {project}/{verison} directory records the metrics about mitigable or notMitigable.