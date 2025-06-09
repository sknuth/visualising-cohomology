# Beaconcha.in Validator Dashboard

This folder provides an example Google Apps Script for a Google Sheet dashboard
that tracks the daily ETH rewards for a set of validators starting from a specific date.
It now also demonstrates how to pull data from the Rocketpool smart contracts
using Alchemy so you can show your RPL stake and smoothing pool rewards next to
the Beaconcha.in figures.

## Setup Steps

1. **Create a new Google Sheet.**
2. Go to **Extensions → Apps Script** and replace the contents of the script editor with `dashboard.gs`.
3. Edit the constants at the top of the script:
   - `validators` – your validator indices
   - `START_DATE` – the donation start date
   - `ALCHEMY_API_KEY` – your Alchemy key
   - `NODE_ADDRESS` – the Rocketpool node address
   - contract addresses for RPL staking and the smoothing pool
4. Save and run `updateRewards` to populate the sheets.

## Notes

- The script uses the public [beaconcha.in](https://beaconcha.in) API for validator rewards.
- Additional calls are made to the Rocketpool contracts via Alchemy to retrieve the node's RPL stake and smoothing pool rewards.
- If any of the APIs change, adjust the URLs or function selectors in `dashboard.gs` accordingly.

