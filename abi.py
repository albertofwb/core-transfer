PLEDGE_AGENT_ADDRESS = "0x0000000000000000000000000000000000001007"
MIN_GAS_PRICE = 0.0007
MAX_GAS_PRICE = 0.1
CORE_RPC_URL = "https://rpc.coredao.org"

CORE_ABI = [
  {
    "inputs": [
      {
        "name": "candidate",
        "internalType": "address",
        "type": "address"
      }
    ],
    "name": "InactiveAgent",
    "type": "error"
  },
  {
    "inputs": [
      {
        "name": "name",
        "internalType": "string",
        "type": "string"
      }
    ],
    "name": "MismatchParamLength",
    "type": "error"
  },
  {
    "inputs": [
      {
        "name": "name",
        "internalType": "string",
        "type": "string"
      },
      {
        "name": "given",
        "internalType": "uint256",
        "type": "uint256"
      },
      {
        "name": "lowerBound",
        "internalType": "uint256",
        "type": "uint256"
      },
      {
        "name": "upperBound",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "name": "OutOfBounds",
    "type": "error"
  },
  {
    "inputs": [
      {
        "name": "source",
        "internalType": "address",
        "type": "address"
      },
      {
        "name": "target",
        "internalType": "address",
        "type": "address"
      }
    ],
    "name": "SameCandidate",
    "type": "error"
  },
  {
    "inputs": [
      {
        "indexed": True,
        "name": "txid",
        "internalType": "bytes32",
        "type": "bytes32"
      },
      {
        "indexed": True,
        "name": "delegator",
        "internalType": "address",
        "type": "address"
      }
    ],
    "name": "btcPledgeExpired",
    "anonymous": False,
    "type": "event"
  },
  {
    "inputs": [
      {
        "indexed": True,
        "name": "delegator",
        "internalType": "address",
        "type": "address"
      },
      {
        "indexed": True,
        "name": "operator",
        "internalType": "address",
        "type": "address"
      },
      {
        "indexed": False,
        "name": "amount",
        "internalType": "uint256",
        "type": "uint256"
      },
      {
        "indexed": False,
        "name": "success",
        "internalType": "bool",
        "type": "bool"
      }
    ],
    "name": "claimedReward",
    "anonymous": False,
    "type": "event"
  },
  {
    "inputs": [
      {
        "indexed": True,
        "name": "txid",
        "internalType": "bytes32",
        "type": "bytes32"
      },
      {
        "indexed": True,
        "name": "agent",
        "internalType": "address",
        "type": "address"
      },
      {
        "indexed": True,
        "name": "delegator",
        "internalType": "address",
        "type": "address"
      },
      {
        "indexed": False,
        "name": "script",
        "internalType": "bytes",
        "type": "bytes"
      },
      {
        "indexed": False,
        "name": "blockHeight",
        "internalType": "uint32",
        "type": "uint32"
      },
      {
        "indexed": False,
        "name": "outputIndex",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "name": "delegatedBtc",
    "anonymous": False,
    "type": "event"
  },
  {
    "inputs": [
      {
        "indexed": True,
        "name": "agent",
        "internalType": "address",
        "type": "address"
      },
      {
        "indexed": True,
        "name": "delegator",
        "internalType": "address",
        "type": "address"
      },
      {
        "indexed": False,
        "name": "amount",
        "internalType": "uint256",
        "type": "uint256"
      },
      {
        "indexed": False,
        "name": "totalAmount",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "name": "delegatedCoin",
    "anonymous": False,
    "type": "event"
  },
  {
    "inputs": [
      {
        "indexed": True,
        "name": "txid",
        "internalType": "bytes32",
        "type": "bytes32"
      },
      {
        "indexed": False,
        "name": "feeReceiver",
        "internalType": "address payable",
        "type": "address"
      },
      {
        "indexed": False,
        "name": "fee",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "name": "failedTransferBtcFee",
    "anonymous": False,
    "type": "event"
  },
  {
    "inputs": [
      {
        "indexed": False,
        "name": "key",
        "internalType": "string",
        "type": "string"
      },
      {
        "indexed": False,
        "name": "value",
        "internalType": "bytes",
        "type": "bytes"
      }
    ],
    "name": "paramChange",
    "anonymous": False,
    "type": "event"
  },
  {
    "inputs": [
      {
        "indexed": True,
        "name": "agent",
        "internalType": "address",
        "type": "address"
      },
      {
        "indexed": False,
        "name": "coinReward",
        "internalType": "uint256",
        "type": "uint256"
      },
      {
        "indexed": False,
        "name": "powerReward",
        "internalType": "uint256",
        "type": "uint256"
      },
      {
        "indexed": False,
        "name": "btcReward",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "name": "roundReward",
    "anonymous": False,
    "type": "event"
  },
  {
    "inputs": [
      {
        "indexed": True,
        "name": "txid",
        "internalType": "bytes32",
        "type": "bytes32"
      },
      {
        "indexed": False,
        "name": "sourceAgent",
        "internalType": "address",
        "type": "address"
      },
      {
        "indexed": False,
        "name": "targetAgent",
        "internalType": "address",
        "type": "address"
      },
      {
        "indexed": False,
        "name": "delegator",
        "internalType": "address",
        "type": "address"
      },
      {
        "indexed": False,
        "name": "amount",
        "internalType": "uint256",
        "type": "uint256"
      },
      {
        "indexed": False,
        "name": "totalAmount",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "name": "transferredBtc",
    "anonymous": False,
    "type": "event"
  },
  {
    "inputs": [
      {
        "indexed": True,
        "name": "txid",
        "internalType": "bytes32",
        "type": "bytes32"
      },
      {
        "indexed": False,
        "name": "feeReceiver",
        "internalType": "address payable",
        "type": "address"
      },
      {
        "indexed": False,
        "name": "fee",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "name": "transferredBtcFee",
    "anonymous": False,
    "type": "event"
  },
  {
    "inputs": [
      {
        "indexed": True,
        "name": "sourceAgent",
        "internalType": "address",
        "type": "address"
      },
      {
        "indexed": True,
        "name": "targetAgent",
        "internalType": "address",
        "type": "address"
      },
      {
        "indexed": True,
        "name": "delegator",
        "internalType": "address",
        "type": "address"
      },
      {
        "indexed": False,
        "name": "amount",
        "internalType": "uint256",
        "type": "uint256"
      },
      {
        "indexed": False,
        "name": "totalAmount",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "name": "transferredCoin",
    "anonymous": False,
    "type": "event"
  },
  {
    "inputs": [
      {
        "indexed": True,
        "name": "agent",
        "internalType": "address",
        "type": "address"
      },
      {
        "indexed": True,
        "name": "delegator",
        "internalType": "address",
        "type": "address"
      },
      {
        "indexed": False,
        "name": "amount",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "name": "undelegatedCoin",
    "anonymous": False,
    "type": "event"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [],
    "name": "BTC_STAKE_MAGIC",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [],
    "name": "BTC_UNIT_CONVERSION",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "address",
        "type": "address"
      }
    ],
    "inputs": [],
    "name": "BURN_ADDR",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "address",
        "type": "address"
      }
    ],
    "inputs": [],
    "name": "CANDIDATE_HUB_ADDR",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [],
    "name": "CHAINID",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "int256",
        "type": "int256"
      }
    ],
    "inputs": [],
    "name": "CLAIM_ROUND_LIMIT",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [],
    "name": "FEE_FACTOR",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "address",
        "type": "address"
      }
    ],
    "inputs": [],
    "name": "FOUNDATION_ADDR",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "address",
        "type": "address"
      }
    ],
    "inputs": [],
    "name": "GOV_HUB_ADDR",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint32",
        "type": "uint32"
      }
    ],
    "inputs": [],
    "name": "INIT_BTC_CONFIRM_BLOCK",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [],
    "name": "INIT_BTC_FACTOR",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [],
    "name": "INIT_DELEGATE_BTC_GAS_PRICE",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [],
    "name": "INIT_HASH_POWER_FACTOR",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [],
    "name": "INIT_MIN_BTC_LOCK_ROUND",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [],
    "name": "INIT_MIN_BTC_VALUE",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [],
    "name": "INIT_REQUIRED_COIN_DEPOSIT",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "address",
        "type": "address"
      }
    ],
    "inputs": [],
    "name": "LIGHT_CLIENT_ADDR",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "address",
        "type": "address"
      }
    ],
    "inputs": [],
    "name": "PLEDGE_AGENT_ADDR",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [],
    "name": "POWER_BLOCK_FACTOR",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "address",
        "type": "address"
      }
    ],
    "inputs": [],
    "name": "RELAYER_HUB_ADDR",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [],
    "name": "ROUND_INTERVAL",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "address",
        "type": "address"
      }
    ],
    "inputs": [],
    "name": "SLASH_CONTRACT_ADDR",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "address",
        "type": "address"
      }
    ],
    "inputs": [],
    "name": "SYSTEM_REWARD_ADDR",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "address",
        "type": "address"
      }
    ],
    "inputs": [],
    "name": "VALIDATOR_CONTRACT_ADDR",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [],
    "inputs": [
      {
        "name": "agentList",
        "internalType": "address[]",
        "type": "address[]"
      },
      {
        "name": "rewardList",
        "internalType": "uint256[]",
        "type": "uint256[]"
      }
    ],
    "name": "addRoundReward",
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "totalDeposit",
        "internalType": "uint256",
        "type": "uint256"
      },
      {
        "name": "power",
        "internalType": "uint256",
        "type": "uint256"
      },
      {
        "name": "coin",
        "internalType": "uint256",
        "type": "uint256"
      },
      {
        "name": "btc",
        "internalType": "uint256",
        "type": "uint256"
      },
      {
        "name": "totalBtc",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [
      {
        "name": "",
        "internalType": "address",
        "type": "address"
      }
    ],
    "name": "agentsMap",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "bool",
        "type": "bool"
      }
    ],
    "inputs": [],
    "name": "alreadyInit",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "address",
        "type": "address"
      }
    ],
    "inputs": [
      {
        "name": "",
        "internalType": "bytes20",
        "type": "bytes20"
      }
    ],
    "name": "btc2ethMap",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint32",
        "type": "uint32"
      }
    ],
    "inputs": [],
    "name": "btcConfirmBlock",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [],
    "name": "btcFactor",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "agent",
        "internalType": "address",
        "type": "address"
      },
      {
        "name": "delegator",
        "internalType": "address",
        "type": "address"
      },
      {
        "name": "value",
        "internalType": "uint256",
        "type": "uint256"
      },
      {
        "name": "endRound",
        "internalType": "uint256",
        "type": "uint256"
      },
      {
        "name": "rewardIndex",
        "internalType": "uint256",
        "type": "uint256"
      },
      {
        "name": "feeReceiver",
        "internalType": "address payable",
        "type": "address"
      },
      {
        "name": "fee",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [
      {
        "name": "",
        "internalType": "bytes32",
        "type": "bytes32"
      }
    ],
    "name": "btcReceiptMap",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "rewardSum",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [
      {
        "name": "txidList",
        "internalType": "bytes32[]",
        "type": "bytes32[]"
      }
    ],
    "name": "claimBtcReward",
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      },
      {
        "name": "",
        "internalType": "bool",
        "type": "bool"
      }
    ],
    "inputs": [
      {
        "name": "agentList",
        "internalType": "address[]",
        "type": "address[]"
      }
    ],
    "name": "claimReward",
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      },
      {
        "name": "",
        "internalType": "address",
        "type": "address"
      }
    ],
    "name": "debtDepositMap",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [],
    "inputs": [
      {
        "name": "btcTx",
        "internalType": "bytes",
        "type": "bytes"
      },
      {
        "name": "blockHeight",
        "internalType": "uint32",
        "type": "uint32"
      },
      {
        "name": "nodes",
        "internalType": "bytes32[]",
        "type": "bytes32[]"
      },
      {
        "name": "index",
        "internalType": "uint256",
        "type": "uint256"
      },
      {
        "name": "script",
        "internalType": "bytes",
        "type": "bytes"
      }
    ],
    "name": "delegateBtc",
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [],
    "name": "delegateBtcGasPrice",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [],
    "inputs": [
      {
        "name": "agent",
        "internalType": "address",
        "type": "address"
      }
    ],
    "name": "delegateCoin",
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "outputs": [],
    "inputs": [
      {
        "name": "candidate",
        "internalType": "address",
        "type": "address"
      },
      {
        "name": "miners",
        "internalType": "address[]",
        "type": "address[]"
      }
    ],
    "name": "distributePowerReward",
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "outputs": [
      {
        "components": [
          {
            "name": "deposit",
            "internalType": "uint256",
            "type": "uint256"
          },
          {
            "name": "newDeposit",
            "internalType": "uint256",
            "type": "uint256"
          },
          {
            "name": "changeRound",
            "internalType": "uint256",
            "type": "uint256"
          },
          {
            "name": "rewardIndex",
            "internalType": "uint256",
            "type": "uint256"
          },
          {
            "name": "transferOutDeposit",
            "internalType": "uint256",
            "type": "uint256"
          },
          {
            "name": "transferInDeposit",
            "internalType": "uint256",
            "type": "uint256"
          }
        ],
        "name": "",
        "internalType": "struct PledgeAgent.CoinDelegator",
        "type": "tuple"
      }
    ],
    "inputs": [
      {
        "name": "agent",
        "internalType": "address",
        "type": "address"
      },
      {
        "name": "delegator",
        "internalType": "address",
        "type": "address"
      }
    ],
    "name": "getDelegator",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [
      {
        "name": "round",
        "internalType": "uint256",
        "type": "uint256"
      },
      {
        "name": "agent",
        "internalType": "address",
        "type": "address"
      }
    ],
    "name": "getExpireValue",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "scores",
        "internalType": "uint256[]",
        "type": "uint256[]"
      }
    ],
    "inputs": [
      {
        "name": "candidates",
        "internalType": "address[]",
        "type": "address[]"
      },
      {
        "name": "powers",
        "internalType": "uint256[]",
        "type": "uint256[]"
      },
      {
        "name": "round",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "name": "getHybridScore",
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "outputs": [
      {
        "components": [
          {
            "name": "totalReward",
            "internalType": "uint256",
            "type": "uint256"
          },
          {
            "name": "remainReward",
            "internalType": "uint256",
            "type": "uint256"
          },
          {
            "name": "score",
            "internalType": "uint256",
            "type": "uint256"
          },
          {
            "name": "coin",
            "internalType": "uint256",
            "type": "uint256"
          },
          {
            "name": "round",
            "internalType": "uint256",
            "type": "uint256"
          }
        ],
        "name": "",
        "internalType": "struct PledgeAgent.Reward",
        "type": "tuple"
      }
    ],
    "inputs": [
      {
        "name": "agent",
        "internalType": "address",
        "type": "address"
      },
      {
        "name": "index",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "name": "getReward",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [],
    "inputs": [],
    "name": "init",
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [],
    "name": "minBtcLockRound",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [],
    "name": "minBtcValue",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [],
    "inputs": [
      {
        "name": "agent",
        "internalType": "address",
        "type": "address"
      }
    ],
    "name": "onFelony",
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [],
    "name": "powerFactor",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [],
    "name": "requiredCoinDeposit",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [
      {
        "name": "",
        "internalType": "address",
        "type": "address"
      }
    ],
    "name": "rewardMap",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [],
    "name": "roundTag",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [],
    "inputs": [
      {
        "name": "validators",
        "internalType": "address[]",
        "type": "address[]"
      },
      {
        "name": "round",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "name": "setNewRound",
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "outputs": [
      {
        "name": "power",
        "internalType": "uint256",
        "type": "uint256"
      },
      {
        "name": "coin",
        "internalType": "uint256",
        "type": "uint256"
      },
      {
        "name": "powerFactor",
        "internalType": "uint256",
        "type": "uint256"
      },
      {
        "name": "btc",
        "internalType": "uint256",
        "type": "uint256"
      },
      {
        "name": "btcFactor",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "inputs": [
      {
        "name": "",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "name": "stateMap",
    "stateMutability": "view",
    "type": "function"
  },
  {
    "outputs": [],
    "inputs": [
      {
        "name": "txid",
        "internalType": "bytes32",
        "type": "bytes32"
      },
      {
        "name": "targetAgent",
        "internalType": "address",
        "type": "address"
      }
    ],
    "name": "transferBtc",
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "outputs": [],
    "inputs": [
      {
        "name": "sourceAgent",
        "internalType": "address",
        "type": "address"
      },
      {
        "name": "targetAgent",
        "internalType": "address",
        "type": "address"
      },
      {
        "name": "amount",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "name": "transferCoin",
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "outputs": [],
    "inputs": [
      {
        "name": "sourceAgent",
        "internalType": "address",
        "type": "address"
      },
      {
        "name": "targetAgent",
        "internalType": "address",
        "type": "address"
      }
    ],
    "name": "transferCoin",
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "outputs": [],
    "inputs": [
      {
        "name": "agent",
        "internalType": "address",
        "type": "address"
      }
    ],
    "name": "undelegateCoin",
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "outputs": [],
    "inputs": [
      {
        "name": "agent",
        "internalType": "address",
        "type": "address"
      },
      {
        "name": "amount",
        "internalType": "uint256",
        "type": "uint256"
      }
    ],
    "name": "undelegateCoin",
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "outputs": [],
    "inputs": [
      {
        "name": "key",
        "internalType": "string",
        "type": "string"
      },
      {
        "name": "value",
        "internalType": "bytes",
        "type": "bytes"
      }
    ],
    "name": "updateParam",
    "stateMutability": "nonpayable",
    "type": "function"
  }
]