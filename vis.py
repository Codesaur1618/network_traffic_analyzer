import matplotlib.pyplot as plt

def visualize_protocol_distribution(protocol_counts):
    protocols = list(protocol_counts.keys())
    counts = list(protocol_counts.values())

    plt.bar(protocols, counts, color='blue')
    plt.xlabel('Protocol')
    plt.ylabel('Packet Count')
    plt.title('Protocol Distribution in Captured Packets')
    plt.show()

def visualize_response_type_distribution(response_types):
    labels = list(response_types.keys())
    counts = list(response_types.values())

    plt.bar(labels, counts, color='green')
    plt.xlabel('MDNS Response Type')
    plt.ylabel('Count')
    plt.title('Distribution of MDNS Response Types')
    plt.show()

def visualize_response_length_distribution(response_lengths):
    plt.hist(response_lengths, bins=20, color='purple', alpha=0.7)
    plt.xlabel('Response Length')
    plt.ylabel('Count')
    plt.title('Distribution of MDNS Response Lengths')
    plt.show()

def visualize_protocol_pie_chart(protocol_counts):
    labels = list(protocol_counts.keys())
    counts = list(protocol_counts.values())

    plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90, colors=['gold', 'lightskyblue', 'lightcoral'])
    plt.title('Protocol Distribution (Pie Chart)')
    plt.show()

# Example protocol counts (replace with your actual counts)
protocol_counts = {'MDNS': 10, 'TCP': 5, 'UDP': 3, 'ICMP': 2}

# Example MDNS response data (replace with your actual data)
mdns_responses = [
    {'response_type': 'PTR', 'response_length': 150},
    {'response_type': 'A', 'response_length': 80},
    # Add more MDNS responses as needed
]

# Extract response types and lengths
response_types = {}
response_lengths = []

for response in mdns_responses:
    r_type = response['response_type']
    response_lengths.append(response['response_length'])

    if r_type in response_types:
        response_types[r_type] += 1
    else:
        response_types[r_type] = 1

# Example visualizations
visualize_protocol_distribution(protocol_counts)
visualize_response_type_distribution(response_types)
visualize_response_length_distribution(response_lengths)
visualize_protocol_pie_chart(protocol_counts)

