// Web3 Integration for MetaMask
async function connectMetaMask() {
  if (typeof window.ethereum !== 'undefined') {
    try {
      const accounts = await window.ethereum.request({
        method: 'eth_requestAccounts'
      });
      console.log('MetaMask connected:', accounts[0]);
      return accounts[0];
    } catch (error) {
      console.error('MetaMask connection failed:', error);
    }
  } else {
    console.log('MetaMask not installed');
  }
}

// Get current account
async function getCurrentAccount() {
  if (typeof window.ethereum !== 'undefined') {
    const accounts = await window.ethereum.request({
      method: 'eth_accounts'
    });
    return accounts[0] || null;
  }
  return null;
}
