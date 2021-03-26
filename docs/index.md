# CFDE-Submit

The `cfde-submit` tool is a product of the NIH [Common Fund Data Ecosystem (CFDE)](https://www.nih-cfde.org/) Coordinating Center (CFDE-CC).

This lightweight command-line tool enables an authorized NIH Common Fund Data Coordinating Center (DCC) to submit its data inventory information to the CFDE Portal, where it can be reviewed and ultimately approved for public viewing.

The `cfde-submit` tool works with the CFDE Portal, and its use is authorized by the CFDE-CC team: only authorized individuals may submit information using `cfde-submit`. See the Getting Started section for information about obtaining authorization.

## Install

See the [Install Guide](./install/index.md) for installation instructions.

---

## Get started

This section covers everything you need to do after you've installed the `cfde-submit` tool and before you use it to perform a submission. If you are using `cfde-submit` on behalf of a single DCC, you will only need to do these things once. Otherwise, you'll re-do these things the first time you submit on behalf of a new DCC.

### Terminology

The [Common Fund Data Ecosystem (CFDE)](https://www.nih-cfde.org/) is an initiative of the National Institutes of Health's Common Fund. The Common Fund sponsors several large biomedical initiatives that either span multiple institutes or have no institute as a home. Each of these initiatives is focused on a specific biomedical research issue. For example, the [Kids First](https://kidsfirstdrc.org/) initiative is focused on pediatric cancer and birth defects, and the [SPARC](https://commonfund.nih.gov/sparc/sparc4-sp4) initiative focuses on interconnections and interactions between the human nervous system and specific organs.

Within each Common Fund initiative, a **Data Coordinating Center (DCC)** is responsible for gathering the data produced by initiative partners and making that data available to the research community at large, subject to data access agreements. Each Common Fund DCC currently uses its own methods and tools to carry out its mission, so researchers who need to access data must work directly with each relevant DCC, and may need to familiarize themselves with several different data access systems.

CFDE's goal is to make it easier for researchers to discover and use Common Fund data. The **CFDE Coordinating Center (CFDE-CC)** provides a website, the **[CFDE Portal](https://app.nih-cfde.org/)**, to discover data available from the Common Fund, and is also working with each DCC to establish consistent data access mechanisms.

Each DCC tells the CFDE Portal about the data they manage and make available to researchers. CFDE has defined a model for DCCs to use when describing their data holdings: the **[Crosscut Metadata Model (C2M2)](https://docs.nih-cfde.org/en/latest/c2m2/draft-C2M2_specification/)**. A description of a DCC's data in the C2M2 model is called a **C2M2 instance**. The `cfde-submit` tool is the mechanism by which a DCC shares a new (revised or expanded) C2M2 instance with the CFDE Portal.

### Register your DCC

To submit a C2M2 instance for your DCC, your DCC must first be registered with the CFDE Portal. Contact the CFDE-CC's DCC Engagement team to register your DCC.

### Obtain authorization to use `cfde-submit`

Once your DCC has been registered with CFDE, your Principal Investigator (or designee) will be given the ability to add team members to permission groups for the DCC. To use the `cfde-submit` tool, you must be added to your DCC's Submitters group.  The CFDE-CC's DCC Engagement team can step you and your Principal Investigator through this process.

### Prepare your C2M2 instance

The `cfde-submit` tool takes a valid C2M2 instance as its input. Any any given time, each DCC has a single C2M2 instance visible in the CFDE portal's public views. Of course, you may revise your DCC's C2M2 instance when your DCC's data changes. You may submit several versions of your DCC's C2M2 instance and review each in a private Data Review area in the portal before approving a single instance for use in the public portal views.

Constructing a C2M2 instance requires comprehensive knowledge of your DCC's data. The [C2M2 documentation](https://docs.nih-cfde.org/en/latest/c2m2/draft-C2M2_specification/) describes the data model and how to construct a C2M2 instance for your DCC's data.

When using the `cfde-submit` tool, your C2M2 instance must be contained in a folder on your computer, and it must include the JSON Schema document appropriate for the type of C2M2 instance you are submitting. 

<[TODO: Add detail about any extra files that need to be included in the C2M2 datapackage. E.g., DCC and contact info.]>

### Find your DCC's identifier

When using `cfde-submit` to submit a new C2M2 instance, you must enter your DCC's unique identifier, issued by CFDE-CC. You can find this identifier in the CFDE Portal. Visit the [Onboarded DCC](https://app.nih-cfde.org/chaise/recordset/#registry/CFDE:dcc@sort(RID)) page in the CFDE Portal and locate your DCC in the table.

The identifier you need for `cfde-submit` is of the form `cfde_registry_dcc:*`, where the `*` is replaced by a short form of your DCC's name. For example, the DCC identifier for The Human Microbiome Project is `cfde_registry_dcc:hmp`.

<[TODO: The link above will not work until the production portal has been updated. When the production portal is updated, make sure it works!]>

### Check your system

Here are a few things that could make `cfde-submit` not work correctly on your system.

If you have [Globus Connect Personal](https://www.globus.org/globus-connect-personal) installed on your computer, `cfde-submit` will attempt to use it to transfer your C2M2 instance to CFDE.

* Make sure Globus Connect Personal is running. If it is installed but not running, `cfde-submit` will start a transfer, but the transfer will not begin until you start Globus Connect Personal.
* Make sure Globus Connect Personal has access to the folder where your C2M2 instance resides on your system. By default, Globus Connect Personal has access to your home directory on the system and everything within it. If your data is not somewhere within your home directory, or if you have changed the Preferences for Globus Connect Personal to customize its access on your system, there is a good chance `cfde-submit` will not be able to transfer your C2M2 instance. Move the C2M2 instance folder to your home directory or set the Access Preferences in Globus Connect Personal to provide access to the C2M2 instance folder.

---

## Use the tool

Once you've created a C2M2 instance, the next steps are to submit it to the CFDE Portal, review it, and--assuming it is satisfactory--approve it (or have someone in your DCC approve it) for public viewing. This section walks through the submission process.

### Login

Submitting a new C2M2 instance for your DCC requires authorization, so the first step when using `cfde-submit` is to login.

> NOTE: Logging in requires a web browser, but it can be done in a remote terminal shell as long as you have a web browser on your local system.

> NOTE: If you use another `cfde-submit` command without being logged in, it will automatically start the login process. We recommend using the login command anyway unless you believe you are logged in already.

To login, enter the following command.

```
 cfde-submit login
```

> NOTE: If you are already logged in, `cfde-submit login` will validate your previous login and display a message telling you you're already logged in.

If you aren't already logged in, the login process will begin. The login process will vary depending on whether or not you have a web browser on the system where you are running `cfde-submit`.

If you run `cfde-submit login` on a computer with a web browser, your browser will automatically open to a login page. Make sure you login using the same identity you used when you completed the section [Obtain authorization to use cfde-submit](#Obtain-authorization-to-use-cfde-submit) above. When your login completes, you may close your web browser window. `cfde-submit` will display a message stating that you are logged in and then exit.

If you run `cfde-submit login` in a remote terminal shell, the command will display a web address that you must visit to login and prompt you to enter a code. Copy the web address, open a web browser on your local system, and paste in the address. Make sure you login using the same identity you used when you completed the section [Obtain authorization to use cfde-submit](#Obtain-authorization-to-use-cfde-submit) above. When your login completes, a code will be displayed in the browser window. Copy this code and paste it into the prompt displayed by the `cfde-submit` command. `cfde-submit` will display a message stating that you are logged in and then exit.

### Run

Once logged in, the next step is to submit your C2M2 instance to the CFDE Portal. Use the following command to begin a submission.

```
cfde-submit run DATA-PATH [OPTIONS]
```

Replace `DATA-PATH` with the directory in which your C2M2 instance is located.

This command will automatically do the following things.

- It will check to make sure the directory you specified has the expected files in it.
- It will create a [BDBag](https://bd2k.ini.usc.edu/tools/bdbag/) with the contents of your C2M2 instance in it.
- It will upload a copy of the BDBag to the CFDE-CC's server.
- It will begin the automated processes that ingest the new C2M2 instance into a review catalog in the CFDE Portal.
- It will let you know if the above steps were successful or not and exit.

> Normally, the upload step above will upload the BDBag to CFDE-CC's server while the command runs, and you will notice a pause while the data is uploaded. The command will not complete until the upload has finished. If you have [Globus Connect Personal](https://www.globus.org/globus-connect-personal) installed, `cfde-submit run` will hand the upload off to Globus and will exit successfully as soon as the upload request is made. The upload will happen in the background as long as Globus Connect Personal is running. You may quit Globus Connect Personal (or shut your system down) before the upload completes and the upload will resume when you restart Globus Connect Personal. You will receive an email message when the upload completes.

You can specify the following `OPTIONS` with `cfde-submit run`.

  - ``--output-dir=OUTPUT_DIR`` will copy the data in ``DATA-PATH``, if it is a
    directory, to the location you specify, which must not exist and must not
    be inside ``DATA-PATH``. The resulting BDBag will be named after the output
    directory. If not specified, the BDBag will be created in-place in
    ``DATA_PATH`` if necessary.
  - ``--delete-dir`` will trigger deletion of the ``output-dir`` after processing
    is complete. If you didn't specify ``output-dir``, this option has no effect.
  - ``--ignore-git`` will prevent the client from overwriting ``output-dir`` and ``delete-dir`` to handle Git repositories.
  - ``--force-http`` will prevent use of Globus Connect Personal if it is installed. The command will not complete until your data has been uploaded.

### Status

The `cfde-submit run` command will exist as soon as your C2M2 instance has been uploaded and the automated ingest process begins. You can check the status of the ingest process using the following command.

```
cfde-submit status [OPTIONS]
```

With no `[OPTIONS]`, this will display the status of your most recent `cfde-submit run` command.

The status includes an *Instance ID*, which is a long string of numbers, letters, and dashes. (You can ignore the *Flow ID*.) Each `cfde-submit run` command has its own Instance ID, and you can use this Instance ID to check the status of earlier submissions rather than the most recent one.

You can specify the following `[OPTIONS]` with `cfde-submit status`.

  - ``--flow-instance-id=ID`` is the ID of the particular submission.
  - ``--flow-id=ID`` is the ID of the Flow (NOT a specific submission).

### After your submission

Shortly after your `cfde-submit run` command completes, you will be able to use the CFDE Portal's Data Review features to see the new submission. Visit the CFDE Portal, make sure you are logged in (click the Log In button in the upper-right corner of the page), and click **Data Review** on the right side of the main navigation bar. Your new submission should appear at or near the top of the list.

Under **Status Summary**, the **Ingest Status** field will show what is happening with your submission. When Ingest Status says "content ready for review," you should see additional links for **Browse Data**, **Summary Charts**, and **Raw Data**. Use these links to review your submission. Note that the Raw Data link provides a download of the BDBag that was created when you ran ``cfde-submit run``, so you can always retrieve a copy of your input data.

### Logout

When you are finished using ``cfde-submit``, you can logout using the following command.

```
cfde-submit logout
```

Subsequent ``cfde-submit`` commands will require a fresh login.

### Version
Specifying the --version flag will print the cfde-submit version number and exit.

```
cfde-submit --version
```

### Reset
The reset command resets your cfde-submit configuration. This can be useful in some cases, for 
example if you want to unset the default DCC.

```
cfde-submit reset
```

### Updating
To update the cfde-submit package to the latest version, run the command below.

```
python3 -m pip install --upgrade cfde-submit
```
