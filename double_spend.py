import matplotlib.pyplot as plt
import numpy as np

def ev_attack_success(attacker_ratio, attack_payoff):
    return (attacker_ratio**2) * attack_payoff

def ev_attack_block_reward(attacker_ratio, block_reward):
    return attacker_ratio * block_reward


total_validators = 1000
total_attackers = 100
total_defenders = total_validators - total_attackers

attacker_ratio = total_attackers / total_validators
defender_ratio = 1 - attacker_ratio

num_samples = 1001
largest_attack_payoff = 10000000

attack_payoffs = np.linspace(0, largest_attack_payoff, num_samples)

#source https://decrypt.co/57740/bitcoin-miners-now-earn-1-btc-in-fees-per-block
transaction_fee = 48000


block_reward_btc = 6.25
bitcoin_price_usd = 50000
block_reward_usd = block_reward_btc * bitcoin_price_usd + transaction_fee

ratios = [.05, .1, .25, .5]

for i in range(len(ratios)):
    ax = plt.subplot(2, 2, i + 1)
    ax.plot(attack_payoffs, ev_attack_success(ratios[i], attack_payoffs), label = "EV Attack Reward")
    ev_non_attack_br = ev_attack_block_reward(ratios[i], block_reward_usd)
    ev_attack_block_reward_arr = np.full(num_samples, ev_non_attack_br)
    ax.plot(attack_payoffs, ev_attack_block_reward_arr, label = "EV Block Reward")
    ax.legend(prop={'size': 5})
    ax.set_xticklabels(attack_payoffs, fontsize=5)
    ax.set_yticklabels(attack_payoffs, fontsize=5)
    ax.set_xlabel("Attacking Payoff", font = {'size' : 7})
    ax.set_ylabel("Expected Value", font = {'size' : 7})
    ax.set_title("Expected Value: k/N = {}".format(ratios[i]), font = {'size' : 10})

plt.tight_layout()
plt.savefig('EV_attack.png')
plt.show()






