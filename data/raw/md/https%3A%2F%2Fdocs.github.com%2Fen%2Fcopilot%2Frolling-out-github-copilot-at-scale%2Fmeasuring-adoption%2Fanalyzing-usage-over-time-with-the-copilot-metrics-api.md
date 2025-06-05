  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Roll out Copilot at scale](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale "Roll out Copilot at scale")/
  * [Measuring adoption](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/measuring-adoption "Measuring adoption")/
  * [Analyze usage over time](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/measuring-adoption/analyzing-usage-over-time-with-the-copilot-metrics-api "Analyze usage over time")


# Analyzing usage over time with the Copilot metrics API
Learn how to connect to the API, store data, and analyze usage trends.
## Who can use this feature?
Organization owners, enterprise owners, and billing managers
GitHub Copilot Business or GitHub Copilot Enterprise
## In this article
  * [Introduction](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/measuring-adoption/analyzing-usage-over-time-with-the-copilot-metrics-api#introduction)
  * [About endpoint availability](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/measuring-adoption/analyzing-usage-over-time-with-the-copilot-metrics-api#about-endpoint-availability)
  * [Prerequisites](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/measuring-adoption/analyzing-usage-over-time-with-the-copilot-metrics-api#prerequisites)
  * [1. Create a personal access token](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/measuring-adoption/analyzing-usage-over-time-with-the-copilot-metrics-api#1-create-a-personal-access-token)
  * [2. Connect to the API](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/measuring-adoption/analyzing-usage-over-time-with-the-copilot-metrics-api#2-connect-to-the-api)
  * [3. Store the data](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/measuring-adoption/analyzing-usage-over-time-with-the-copilot-metrics-api#3-store-the-data)
  * [4. Analyze trends](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/measuring-adoption/analyzing-usage-over-time-with-the-copilot-metrics-api#4-analyze-trends)


## [Introduction](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/measuring-adoption/analyzing-usage-over-time-with-the-copilot-metrics-api#introduction)
You can use the [REST API endpoints for Copilot metrics](https://docs.github.com/en/rest/copilot/copilot-metrics) to see trends in how users are adopting GitHub Copilot. During a rollout of GitHub Copilot, it's useful to view these trends to check that people are using their assigned licenses, see which features people are using, and understand the effect of your company's enablement plan on developers.
The API includes:
  * Data for the last 28 days
  * Numbers of active users and engaged users
  * Breakdowns by language and IDE
  * The option to view metrics for an enterprise, organization, or team


This guide demonstrates how to query the API, store data, and analyze a trend for changes to the number of users per week. The examples in this guide use the endpoint for an organization, but you can adapt the examples to meet your needs.
## [About endpoint availability](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/measuring-adoption/analyzing-usage-over-time-with-the-copilot-metrics-api#about-endpoint-availability)
Endpoints are available to get data for an enterprise, organization, organization team, or enterprise team on GitHub.com.
  * If you have a Copilot Business or Copilot Enterprise plan as part of a regular organization or enterprise, you can use the endpoints for **an enterprise, an organization, or an organization team**. You don't have access to enterprise teams unless you're enrolled in a preview.
  * If you use a dedicated enterprise for GitHub Copilot Business—an enterprise account without the ability to create organizations—you can use the endpoints for **an enterprise or an enterprise team**.


The Copilot metrics endpoints are **not** available for GitHub Enterprise Cloud with data residency on GHE.com.
## [Prerequisites](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/measuring-adoption/analyzing-usage-over-time-with-the-copilot-metrics-api#prerequisites)
  * The **Copilot metrics API access** policy must be enabled for your enterprise or organization. See [Managing policies for Copilot in your organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization) or [Managing policies and features for Copilot in your enterprise](https://docs.github.com/en/enterprise-cloud@latest/copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-policies-and-features-for-copilot-in-your-enterprise).
  * The organization, enterprise, or team that you're querying must have enough active Copilot users. The API only returns results for a given day if there are **five or more members with active Copilot licenses** for that day.
  * In this example, we'll create a JavaScript script for querying and analyzing the data. To run this script locally, you must install [Node.js](https://nodejs.org/en), then install the [Octokit.js SDK](https://github.com/octokit/octokit.js#usage) with `npm install -g octokit`.


## [1. Create a personal access token](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/measuring-adoption/analyzing-usage-over-time-with-the-copilot-metrics-api#1-create-a-personal-access-token)
For our example, to get metrics for an organization, we'll create a personal access token (classic) with the `manage_billing:copilot` scope. See [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic).
If you're using another endpoint, you may need different scopes. See [REST API endpoints for Copilot metrics](https://docs.github.com/en/rest/copilot/copilot-metrics).
## [2. Connect to the API](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/measuring-adoption/analyzing-usage-over-time-with-the-copilot-metrics-api#2-connect-to-the-api)
We will call the API from a script and save the response as a variable. We can then store the data externally and analyze trends in the data.
The following example uses the [Octokit client](https://github.com/octokit) for JavaScript. You can use other methods to call the API, such as cURL or the GitHub CLI.
### [Example](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/measuring-adoption/analyzing-usage-over-time-with-the-copilot-metrics-api#example)
In this example:
  * Replace YOUR_TOKEN with your personal access token.
  * Replace YOUR_ORG with your organization name, such as `octo-org`.


JavaScript
BesideInline
```
// Import Octokit
import { Octokit } from "octokit";

// Set your token and organization
const octokit = new Octokit({
  auth: 'YOUR_TOKEN'
});
const org = 'YOUR_ORG';

// Set other variables if required for the endpoint you're using
/*
const team = 'YOUR_TEAM';
const enterprise = 'YOUR_ENTERPRISE';
const entTeam = 'YOUR_ENTERPRISE_TEAM';
*/

// Call the API
async function orgMetrics() {
  const resp = await octokit.request(`GET /orgs/${org}/copilot/metrics`, {
    org: 'ORG',
    headers: {
      'X-GitHub-Api-Version': '2022-11-28'
    }
  });

  const copilotUsage = resp.data;

  console.log(copilotUsage);
  }

// Call the function
orgMetrics();

```

```
import { Octokit } from "octokit";
```

Import Octokit
```
const octokit = new Octokit({
  auth: 'YOUR_TOKEN'
});
const org = 'YOUR_ORG';
```

Set your token and organization
```
/*
const team = 'YOUR_TEAM';
const enterprise = 'YOUR_ENTERPRISE';
const entTeam = 'YOUR_ENTERPRISE_TEAM';
*/
```

Set other variables if required for the endpoint you're using
```
async function orgMetrics(const resp = await octokit.request(`GET /orgs/${org}/copilot/metrics`, {
    org: 'ORG',
    headers: {
      'X-GitHub-Api-Version': '2022-11-28'
    }
  });
  const copilotUsage = resp.data;
  console.log(copilotUsage);
  }
```

Call the API
```
orgMetrics();
```

Call the function
```
// Import Octokit
import { Octokit } from "octokit";

// Set your token and organization
const octokit = new Octokit({
  auth: 'YOUR_TOKEN'
});
const org = 'YOUR_ORG';

// Set other variables if required for the endpoint you're using
/*
const team = 'YOUR_TEAM';
const enterprise = 'YOUR_ENTERPRISE';
const entTeam = 'YOUR_ENTERPRISE_TEAM';
*/

// Call the API
async function orgMetrics(const resp = await octokit.request(`GET /orgs/${org}/copilot/metrics`, {
    org: 'ORG',
    headers: {
      'X-GitHub-Api-Version': '2022-11-28'
    }
  });

  const copilotUsage = resp.data;

  console.log(copilotUsage);
  }

// Call the function
orgMetrics();

```

### [Run the script locally](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/measuring-adoption/analyzing-usage-over-time-with-the-copilot-metrics-api#run-the-script-locally)
To test the script locally, save the file as `copilot.mjs`, then run `node copilot.mjs`.
The **.mjs** file type is important. The `import { Octokit }` statement may not work with a regular `.js` file.
In your terminal, you should see output with a JSON array like the following.
```
[
  {
    date: '2024-11-07',
    copilot_ide_chat: { editors: [Array], total_engaged_users: 14 },
    total_active_users: 28,
    copilot_dotcom_chat: { models: [Array], total_engaged_users: 4 },
    total_engaged_users: 28,
    copilot_dotcom_pull_requests: { total_engaged_users: 0 },
    copilot_ide_code_completions: { editors: [Array], total_engaged_users: 22 }
  },
...

```

## [3. Store the data](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/measuring-adoption/analyzing-usage-over-time-with-the-copilot-metrics-api#3-store-the-data)
To analyze trends over longer than 28 days, you will need to:
  * Call the API daily, using a cron job or scheduled GitHub Actions workflow.
  * Store data locally or with a database service such as MySQL.
  * Query the data to identify trends over time.


### [Example](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/measuring-adoption/analyzing-usage-over-time-with-the-copilot-metrics-api#example-1)
In this example we'll save the data to a local `.json` file. To do this, we will import some modules for working with files, and update the `orgMetrics` function to save the response data.
The function saves new data that is returned each day, without overwriting old data in the file.
New steps are annotated in **bold**.
JavaScript
BesideInline
```
// Import Octokit
import { Octokit } from "octokit";

// **Import modules for working with files**
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

// **Declare variables for working with files**
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Set your token and organization
const octokit = new Octokit({
  auth: 'YOUR_TOKEN'
});

const org = 'YOUR_ORG';

// Call the API
async function orgMetrics() {
  const resp = await octokit.request(`GET /orgs/${org}/copilot/metrics`, {
    org: 'ORG',
    headers: {
      'X-GitHub-Api-Version': '2022-11-28'
    }
  });

  const copilotUsage = resp.data;

  // **Define the path to the local file where data will be stored**
  const dataFilePath = path.join(__dirname, 'copilotMetricsData.json');

  // **Read existing data from the file, if it exists**
  let existingData = [];
  if (fs.existsSync(dataFilePath)) {
    const fileContent = fs.readFileSync(dataFilePath, 'utf8');
    existingData = JSON.parse(fileContent);
  }

  // **Filter out the new data that is not already in the existing data**
  const newData = copilotUsage.filter(entry => !existingData.some(existingEntry => existingEntry.date === entry.date));

  // **Append new data to the existing data**
  if (newData.length > 0) {
    existingData = existingData.concat(newData);

    // **Save the updated data back to the file**
    fs.writeFileSync(dataFilePath, JSON.stringify(existingData, null, 2));
    console.log(`Saved ${newData.length} new entries.`);
  } else {
    console.log('No new data to save.');
  }
}

// Call the function
orgMetrics();

```

```
import { Octokit } from "octokit";
```

Import Octokit
```
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';
import { dirname } from 'path';
```

**Import modules for working with files**
```
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
```

**Declare variables for working with files**
```
const octokit = new Octokit({
  auth: 'YOUR_TOKEN'
});
const org = 'YOUR_ORG';
```

Set your token and organization
```
async function orgMetrics(const resp = await octokit.request(`GET /orgs/${org}/copilot/metrics`, {
    org: 'ORG',
    headers: {
      'X-GitHub-Api-Version': '2022-11-28'
    }
  });
  const copilotUsage = resp.data;
```

Call the API
```
  const dataFilePath = path.join(__dirname, 'copilotMetricsData.json');
```

**Define the path to the local file where data will be stored**
```
  let existingData = [];
  if (fs.existsSync(dataFilePath)) {
    const fileContent = fs.readFileSync(dataFilePath, 'utf8');
    existingData = JSON.parse(fileContent);
  }
```

**Read existing data from the file, if it exists**
```
  const newData = copilotUsage.filter(entry => !existingData.some(existingEntry => existingEntry.date === entry.date));
```

**Filter out the new data that is not already in the existing data**
```
  if (newData.length > 0) {
    existingData = existingData.concat(newData);
```

**Append new data to the existing data**
```
    fs.writeFileSync(dataFilePath, JSON.stringify(existingData, null, 2));
    console.log(`Saved ${newData.length} new entries.`);
  } else {
    console.log('No new data to save.');
  }
}
```

**Save the updated data back to the file**
```
orgMetrics();
```

Call the function
```
// Import Octokit
import { Octokit } from "octokit";

// **Import modules for working with files**
import path from 'path';
import fs from 'fs';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

// **Declare variables for working with files**
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Set your token and organization
const octokit = new Octokit({
  auth: 'YOUR_TOKEN'
});

const org = 'YOUR_ORG';

// Call the API
async function orgMetrics(const resp = await octokit.request(`GET /orgs/${org}/copilot/metrics`, {
    org: 'ORG',
    headers: {
      'X-GitHub-Api-Version': '2022-11-28'
    }
  });

  const copilotUsage = resp.data;

  // **Define the path to the local file where data will be stored**
  const dataFilePath = path.join(__dirname, 'copilotMetricsData.json');

  // **Read existing data from the file, if it exists**
  let existingData = [];
  if (fs.existsSync(dataFilePath)) {
    const fileContent = fs.readFileSync(dataFilePath, 'utf8');
    existingData = JSON.parse(fileContent);
  }

  // **Filter out the new data that is not already in the existing data**
  const newData = copilotUsage.filter(entry => !existingData.some(existingEntry => existingEntry.date === entry.date));

  // **Append new data to the existing data**
  if (newData.length > 0) {
    existingData = existingData.concat(newData);

    // **Save the updated data back to the file**
    fs.writeFileSync(dataFilePath, JSON.stringify(existingData, null, 2));
    console.log(`Saved ${newData.length} new entries.`);
  } else {
    console.log('No new data to save.');
  }
}

// Call the function
orgMetrics();

```

### [Run the script locally](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/measuring-adoption/analyzing-usage-over-time-with-the-copilot-metrics-api#run-the-script-locally-1)
After running the script with `node copilot.mjs`, you should have a new file in your directory called `copilotMetricsData.json`. The file should contain data from the API response.
If you run the script again tomorrow, it should only save data for one new day to the file.
## [4. Analyze trends](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/measuring-adoption/analyzing-usage-over-time-with-the-copilot-metrics-api#4-analyze-trends)
You can work with the data from the API to identify trends over the last 28 days or, if you've stored data from previous API calls, over a longer period.
### [Example](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/measuring-adoption/analyzing-usage-over-time-with-the-copilot-metrics-api#example-2)
In the following example, we update the `orgMetrics` function to extract the total and average number of active and engaged users per week. We could then use that data to track changes over time. This example uses the data returned directly from the API, and doesn't require stored data.
New steps are annotated in **bold**.
JavaScript
BesideInline
```
// Call the API
async function orgMetrics() {
  const resp = await octokit.request(`GET /orgs/${org}/copilot/metrics`, {
    org: 'ORG',
    headers: {
      'X-GitHub-Api-Version': '2022-11-28'
    }
  });

  const copilotUsage = resp.data;

  // **Create an object to store data for each week**
  let userTrends ={
    week1: {
      days:0,
      activeUsers:0,
      engagedUsers:0,
    },
    week2: {
      days:0,
      activeUsers:0,
      engagedUsers:0,
    },
    week3: {
      days:0,
      activeUsers:0,
      engagedUsers:0,
    },
    week4: {
      days:0,
      activeUsers:0,
      engagedUsers:0,
    },
  };

 // **Iterate over the data**
 for (let i =0; i<copilotUsage.length; i++) {
    // **Determine the week number (1-4) based on the index**
    const week = Math.ceil((i+1)/7);
    // **Increment userTrends for the current week**
    userTrends[`week${week}`].days += 1;
    userTrends[`week${week}`].activeUsers += copilotUsage[i].total_active_users;
    userTrends[`week${week}`].engagedUsers += copilotUsage[i].total_engaged_users;
  }

 // **Calculate the average number of active and engaged users per day for each week, rounded to two decimal places**
 for (const week in userTrends) {
  userTrends[week].avgActiveUsers = (userTrends[week].activeUsers / userTrends[week].days).toFixed(2);
  userTrends[week].avgEngagedUsers = (userTrends[week].engagedUsers / userTrends[week].days).toFixed(2);
  }

  // Output to the console
  console.log(userTrends);
}

```

```
async function orgMetrics(const resp = await octokit.request(`GET /orgs/${org}/copilot/metrics`, {
    org: 'ORG',
    headers: {
      'X-GitHub-Api-Version': '2022-11-28'
    }
  });
  const copilotUsage = resp.data;
```

Call the API
```
  let userTrends ={
    week1: {
      days:0,
      activeUsers:0,
      engagedUsers:0,
    },
    week2: {
      days:0,
      activeUsers:0,
      engagedUsers:0,
    },
    week3: {
      days:0,
      activeUsers:0,
      engagedUsers:0,
    },
    week4: {
      days:0,
      activeUsers:0,
      engagedUsers:0,
    },
  };
```

**Create an object to store data for each week**
```
 for (let i =0; i<copilotUsage.length; i++) {
```

**Iterate over the data**
```
    const week = Math.ceil((i+1)/7);
```

**Determine the week number (1-4) based on the index**
```
    userTrends[`week${week}`].days += 1;
    userTrends[`week${week}`].activeUsers += copilotUsage[i].total_active_users;
    userTrends[`week${week}`].engagedUsers += copilotUsage[i].total_engaged_users;
  }
```

**Increment userTrends for the current week**
```
 for (const week in userTrends) {
  userTrends[week].avgActiveUsers = (userTrends[week].activeUsers / userTrends[week].days).toFixed(2);
  userTrends[week].avgEngagedUsers = (userTrends[week].engagedUsers / userTrends[week].days).toFixed(2);
  }
```

**Calculate the average number of active and engaged users per day for each week, rounded to two decimal places**
```
  console.log(userTrends);
}
```

Output to the console
```
// Call the API
async function orgMetrics(const resp = await octokit.request(`GET /orgs/${org}/copilot/metrics`, {
    org: 'ORG',
    headers: {
      'X-GitHub-Api-Version': '2022-11-28'
    }
  });

  const copilotUsage = resp.data;

  // **Create an object to store data for each week**
  let userTrends ={
    week1: {
      days:0,
      activeUsers:0,
      engagedUsers:0,
    },
    week2: {
      days:0,
      activeUsers:0,
      engagedUsers:0,
    },
    week3: {
      days:0,
      activeUsers:0,
      engagedUsers:0,
    },
    week4: {
      days:0,
      activeUsers:0,
      engagedUsers:0,
    },
  };

 // **Iterate over the data**
 for (let i =0; i<copilotUsage.length; i++) {
    // **Determine the week number (1-4) based on the index**
    const week = Math.ceil((i+1)/7);
    // **Increment userTrends for the current week**
    userTrends[`week${week}`].days += 1;
    userTrends[`week${week}`].activeUsers += copilotUsage[i].total_active_users;
    userTrends[`week${week}`].engagedUsers += copilotUsage[i].total_engaged_users;
  }

 // **Calculate the average number of active and engaged users per day for each week, rounded to two decimal places**
 for (const week in userTrends) {
  userTrends[week].avgActiveUsers = (userTrends[week].activeUsers / userTrends[week].days).toFixed(2);
  userTrends[week].avgEngagedUsers = (userTrends[week].engagedUsers / userTrends[week].days).toFixed(2);
  }

  // Output to the console
  console.log(userTrends);
}

```

### [Run the script locally](https://docs.github.com/en/copilot/rolling-out-github-copilot-at-scale/measuring-adoption/analyzing-usage-over-time-with-the-copilot-metrics-api#run-the-script-locally-2)
After running the script with `node copilot.mjs`, you should see output in your terminal like the following.
```
{
  week1: {
    days: 7,
    activeUsers: 174,
    engagedUsers: 174,
    avgActiveUsers: '24.86',
    avgEngagedUsers: '24.86'
  },
  week2: {
    days: 7,
    activeUsers: 160,
    engagedUsers: 151,
    avgActiveUsers: '22.86',
    avgEngagedUsers: '21.57'
  },
  week3: {
    days: 7,
    activeUsers: 134,
    engagedUsers: 123,
    avgActiveUsers: '19.14',
    avgEngagedUsers: '17.57'
  },
  week4: {
    days: 6,
    activeUsers: 143,
    engagedUsers: 132,
    avgActiveUsers: '23.83',
    avgEngagedUsers: '22.00'
  }
}

```

