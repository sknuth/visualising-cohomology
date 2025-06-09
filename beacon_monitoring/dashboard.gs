const API_BASE = 'https://beaconcha.in/api/v1';
const START_DATE = '2025-03-27';

// Alchemy / Rocketpool configuration
const ALCHEMY_API_KEY = 'YOUR_ALCHEMY_KEY';
const ALCHEMY_URL = 'https://eth-mainnet.g.alchemy.com/v2/' + ALCHEMY_API_KEY;
const NODE_ADDRESS = '0xYourNodeAddress';
const RPL_STAKING_CONTRACT = '0xRocketNodeStakingAddress';
const SMOOTHING_POOL_CONTRACT = '0xSmoothingPoolAddress';

function toHexAddress(addr) {
  return addr.replace(/^0x/, '').padStart(64, '0');
}

function ethCall(contract, data) {
  var payload = {
    jsonrpc: '2.0',
    id: 1,
    method: 'eth_call',
    params: [{ to: contract, data: data }, 'latest']
  };
  var options = { method: 'post', contentType: 'application/json', payload: JSON.stringify(payload) };
  var response = UrlFetchApp.fetch(ALCHEMY_URL, options);
  var json = JSON.parse(response.getContentText());
  return json.result;
}

function hexToDecimal(hex) {
  return parseInt(hex, 16);
}

function getRPLStake(address) {
  var selector = '0x9961cee4'; // getNodeRPLStake(address)
  var data = selector + toHexAddress(address);
  var res = ethCall(RPL_STAKING_CONTRACT, data);
  return hexToDecimal(res) / 1e18;
}

function getSmoothingRewards(address) {
  var selector = '0x308e401e'; // getClaimableRewards(address)
  var data = selector + toHexAddress(address);
  var res = ethCall(SMOOTHING_POOL_CONTRACT, data);
  return hexToDecimal(res) / 1e18;
}

function getDailyRewards(validatorIndex, fromDate, toDate) {
  var fromTs = Math.floor(new Date(fromDate).getTime() / 1000);
  var toTs = Math.floor(new Date(toDate).getTime() / 1000);
  var url = API_BASE + '/validator/' + validatorIndex + '/rewards?from=' + fromTs + '&to=' + toTs;
  var response = UrlFetchApp.fetch(url);
  var json = JSON.parse(response.getContentText());
  if (!json.data) {
    return [];
  }
  var rewards = [];
  json.data.forEach(function(item) {
    var day = Utilities.formatDate(new Date(item.day * 1000), Session.getScriptTimeZone(), 'yyyy-MM-dd');
    var reward = item.total / 1e9; // convert from gwei to ETH
    rewards.push([day, reward]);
  });
  return rewards;
}

function updateRewards() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Rewards');
  if (!sheet) {
    sheet = SpreadsheetApp.getActiveSpreadsheet().insertSheet('Rewards');
  }
  var validators = [607618, 697819];
  var endDate = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), 'yyyy-MM-dd');
  var header = ['Date'].concat(validators.map(String));
  sheet.clear();
  sheet.appendRow(header);
  var dateMap = {};
  validators.forEach(function(v) {
    var data = getDailyRewards(v, START_DATE, endDate);
    data.forEach(function(row) {
      var d = row[0];
      if (!dateMap[d]) dateMap[d] = {};
      dateMap[d][v] = row[1];
    });
  });
  var dates = Object.keys(dateMap).sort();
  dates.forEach(function(d) {
    var row = [d];
    validators.forEach(function(v) {
      row.push(dateMap[d][v] || 0);
    });
    sheet.appendRow(row);
  });

  // Summary sheet with Rocketpool data
  var summary = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('Summary');
  if (!summary) {
    summary = SpreadsheetApp.getActiveSpreadsheet().insertSheet('Summary');
  } else {
    summary.clear();
  }
  var rpl = getRPLStake(NODE_ADDRESS);
  var smooth = getSmoothingRewards(NODE_ADDRESS);
  summary.appendRow(['Metric', 'Value']);
  summary.appendRow(['RPL Stake', rpl]);
  summary.appendRow(['Claimable Smoothing Pool ETH', smooth]);
}
