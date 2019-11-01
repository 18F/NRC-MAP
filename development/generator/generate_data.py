import random


def generate_inspections(number_of_inspections):
    """
    Generate synthetic data for Inspections
    This is pre-rc schema based so it is only temporary

    Data will be of the following format:
    id|itaac_status|icn_status|effort_required|facility
    """
    header = "id|itaac_status|icn_status|effort_required|facility"
    itaac_status_options = ["Not Received", "ICN Verified",
                            "UIN Accepted", "ICN Under Review"]
    icn_status_options = ["Received", "Closed", "Resubmittal Req'd"]
    effort_options = range(1, 51)
    facilities = ["VOG 3", "VOG 4"]
    
    data = [header]

    for itaac_id in range(number_of_inspections):

        itaac_status = random.choice(itaac_status_options)
        icn_status = random.choice(icn_status_options)
        effort_required = random.choice(effort_options)
        facility = random.choice(facilities)

        data.append("{}|{}|{}|{}|{}"
            .format(itaac_id, 
                    itaac_status, 
                    icn_status, 
                    effort_required, 
                    facility))


    # write array to file
    with open('/data/inspections.csv', 'w') as f:
        for item in data:
            f.write("%s\n" % item)

if __name__ == '__main__':
    generate_inspections(800)
